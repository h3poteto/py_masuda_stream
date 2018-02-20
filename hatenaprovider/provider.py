from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.oauth.provider import OAuthProvider
import hashlib


class HatenaAccount(ProviderAccount):
    def get_name(self):
        return self.account.extra_data.get('url_name')

    def get_avatar_url(self):
        return self.account.extra_data.get('profile_image_url')

    def to_str(self):
        name = self.get_name()
        return name or super(HatenaAccount, self).to_str()


class HatenaProvider(OAuthProvider):
    id = 'hatena'
    name = 'Hatena'
    account_class = HatenaAccount

    def get_auth_url(self, request, action):
        return 'https://www.hatena.ne.jp/oauth/authorize'

    def extract_uid(self, data):
        return data['url_name']

    def random_email(self, salt):
        return hashlib.sha224(salt.encode()).hexdigest()

    def extract_common_fields(self, data):
        return dict(id=data.get('url_name'),
                    name=data.get('display_name'),
                    email=self.random_email(data.get('url_name')),)


provider_classes = [HatenaProvider]
