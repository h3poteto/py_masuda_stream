import json

from allauth.socialaccount.providers.oauth.client import OAuth
from allauth.socialaccount.providers.oauth.views import (
    OAuthAdapter,
    OAuthCallbackView,
    OAuthLoginView,
)

from .provider import HatenaProvider


class HatenaAPI(OAuth):
    """
    Verifying hatena credentials
    """
    url = 'http://n.hatena.com/applications/my.json'

    def get_user_info(self):
        user = json.loads(self.query(self.url))
        return user


class HatenaOAuthAdapter(OAuthAdapter):
    provider_id = HatenaProvider.id
    request_token_url = 'https://www.hatena.com/oauth/initiate'
    access_token_url = 'https://www.hatena.com/oauth/token'
    authorize_url = 'https://www.hatena.ne.jp/oauth/authorize'

    def complete_login(self, request, app, token, response):
        client = HatenaAPI(request, app.client_id, app.secret,
                           self.request_token_url)
        # access_tokenとしてこんなのが取れる
        # {'oauth_token': 'hoge', 'oauth_token_secret': 'fuga', 'url_name': 'h3poteto', 'display_name': '平仮名3文字ぽてと'}

        extra_data = client.get_user_info()
        return self.get_provider().sociallogin_from_response(request,
                                                             extra_data)


oauth_login = OAuthLoginView.adapter_view(HatenaOAuthAdapter)
oauth_callback = OAuthCallbackView.adapter_view(HatenaOAuthAdapter)
