import json
from django.http import JsonResponse, HttpResponse
from django.views.generic.base import View
from allauth.socialaccount.models import SocialToken
from hatenaprovider.provider import HatenaProvider
from modules.hatena.client import HatenaAPIClient, UnauthorizedError, NotFoundError
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
        try:
            res = api.add_bookmark(params['url'], params['comment'])
        except UnauthorizedError:
            return HttpResponse('Unauthorized', status=401)
        except NotFoundError:
            return HttpResponse('NotFound', status=404)
        return JsonResponse(res)

    @method_decorator(ajax_login_required)
    def get(self, *args, **kwargs):
        #    import pdb; pdb.set_trace()
        token = SocialToken.objects.all().select_related(
            'account',
            'app',
        ).filter(app__provider=HatenaProvider.id).filter(account__user_id=self.request.user.id)[0]

        api = HatenaAPIClient(token.app.client_id, token.app.secret, token.token, token.token_secret)
        try:
            res = api.get_bookmark(self.request.GET.get('url'))
        except UnauthorizedError:
            return HttpResponse('Unauthorized', status=401)
        except NotFoundError:
            return HttpResponse('NotFound', status=404)

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
