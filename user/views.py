from django.http import HttpResponse, JsonResponse
from allauth.socialaccount.models import SocialAccount


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
