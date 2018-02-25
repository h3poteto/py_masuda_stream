from functools import wraps
from django.http import HttpResponse


def ajax_login_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated is True:
            return view_func(request, *args, **kwargs)
        return HttpResponse('Unauthorized', status=401)
    return wrapper
