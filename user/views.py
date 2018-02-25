import json
from django.http import HttpResponse, JsonResponse
from allauth.socialaccount.models import SocialAccount, SocialToken
from hatenaprovider.provider import HatenaProvider
from modules.hatena.client import HatenaAPIClient


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

    api = HatenaAPIClient(token.app.client_id, token.app.secret, token.token, token.token_secret)

    params = json.loads(request.body)
    res = api.bookmark(params['url'], params['comment'])
    return JsonResponse(res)
