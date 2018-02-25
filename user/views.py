import json
import requests
from requests_oauthlib import OAuth1
from django.http import HttpResponse, JsonResponse
from allauth.socialaccount.models import SocialAccount, SocialToken
from hatenaprovider.provider import HatenaProvider


def my(request):
    if request.user.is_authenticated is not True:
        return HttpResponse('Unauthorized', status=401)

    social_account = SocialAccount.objects.get(user_id=request.user.id)
    user = {
        'user': request.user.id,
        'name': request.user.first_name + request.user.last_name,
        'uid': social_account.uid,
        'avatar_url': social_account.get_avatar_url(),
    }
    context = {
        'user': user,
    }
    return JsonResponse(context)


def bookmark(request):
    if request.user.is_authenticated is not True:
        return HttpResponse('Unauthorized', status=401)

    token = SocialToken.objects.all().select_related('account', 'app').filter(app__provider=HatenaProvider.id).filter(account__user_id=request.user.id)[0]

    api = HatenaAPI(token.app.client_id, token.app.secret, token.token, token.token_secret)

    params = json.loads(request.body)
    res = api.bookmark(params['url'], params['comment'])
    return JsonResponse(res)


class HatenaAPI():
    base_url = 'http://api.b.hatena.ne.jp/1'

    def __init__(self, consumer_key, consumer_secret, oauth_token, oauth_token_secret):
        self.oauth = OAuth1(
            consumer_key,
            client_secret=consumer_secret,
            resource_owner_key=oauth_token,
            resource_owner_secret=oauth_token_secret)

    def bookmark(self, target_url, comment):
        path = '/my/bookmark'
        url = self.base_url + path
        params = {
            'url': target_url,
            'comment': comment,
        }

        response = getattr(requests, 'post')(url,
                                             auth=self.oauth,
                                             headers=dict(),
                                             params=params)
#        import pdb; pdb.set_trace()
        response.raise_for_status()

        return response.json()
