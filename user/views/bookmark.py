import json
from django.http import HttpResponse, JsonResponse
from allauth.socialaccount.models import SocialToken
from hatenaprovider.provider import HatenaProvider
from modules.hatena.client import HatenaAPIClient
from django.views.generic.base import View


class Bookmark(View):
    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated is not True:
            return HttpResponse('Unauthorized', status=401)

        token = SocialToken.objects.all().select_related(
            'account',
            'app',
        ).filter(app__provider=HatenaProvider.id).filter(account__user_id=self.request.user.id)[0]

        api = HatenaAPIClient(token.app.client_id, token.app.secret, token.token, token.token_secret)

        params = json.loads(self.request.body)
        res = api.add_bookmark(params['url'], params['comment'])
        return JsonResponse(res)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated is not True:
            return HttpResponse('Unauthorized', status=401)

        #    import pdb; pdb.set_trace()
        token = SocialToken.objects.all().select_related(
            'account',
            'app',
        ).filter(app__provider=HatenaProvider.id).filter(account__user_id=self.request.user.id)[0]

        api = HatenaAPIClient(token.app.client_id, token.app.secret, token.token, token.token_secret)
        res = api.get_bookmark(self.request.GET.get('url'))
        return JsonResponse(res)
