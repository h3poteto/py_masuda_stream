from allauth.socialaccount.providers.oauth.urls import default_urlpatterns

from .provider import HatenaProvider


urlpatterns = default_urlpatterns(HatenaProvider)
