import json
from django.http import JsonResponse
from django.views.generic.base import View
from allauth.socialaccount.models import SocialToken
from hatenaprovider.provider import HatenaProvider
from modules.hatena.client import HatenaAPIClient
from user.decorators import ajax_login_required
from django.utils.decorators import method_decorator


class Bookmark(View):
    @method_decorator(ajax_login_required)
    def post(self, *args, **kwargs):
        token = SocialToken.objects.all().select_related(
            'account',
            'app',
        ).filter(app__provider=HatenaProvider.id).filter(account__user_id=self.request.user.id)[0]

        api = HatenaAPIClient(token.app.client_id, token.app.secret, token.token, token.token_secret)

        params = json.loads(self.request.body)
        res = api.add_bookmark(params['url'], params['comment'])
        return JsonResponse(res)

    @method_decorator(ajax_login_required)
    def get(self, *args, **kwargs):
        #    import pdb; pdb.set_trace()
        token = SocialToken.objects.all().select_related(
            'account',
            'app',
        ).filter(app__provider=HatenaProvider.id).filter(account__user_id=self.request.user.id)[0]

        api = HatenaAPIClient(token.app.client_id, token.app.secret, token.token, token.token_secret)
        res = api.get_bookmark(self.request.GET.get('url'))
        return JsonResponse(res)


@ajax_login_required
def feed(request):
    token = SocialToken.objects.all().select_related(
        'account',
        'app',
    ).filter(app__provider=HatenaProvider.id).filter(account__user_id=request.user.id)[0]

    api = HatenaAPIClient(token.app.client_id, token.app.secret, token.token, token.token_secret)
    res = api.bookmarks()
    return JsonResponse(res)
