from django.http import JsonResponse
from allauth.socialaccount.models import SocialAccount
from user.decorators import ajax_login_required


@ajax_login_required
def my(request):
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
