import requests
from requests_oauthlib import OAuth1


class HatenaAPIClient():
    base_url = 'http://api.b.hatena.ne.jp/1'

    def __init__(self, consumer_key, consumer_secret, oauth_token, oauth_token_secret):
        self.oauth = OAuth1(
            consumer_key,
            client_secret=consumer_secret,
            resource_owner_key=oauth_token,
            resource_owner_secret=oauth_token_secret)

    def add_bookmark(self, target_url, comment):
        path = '/my/bookmark'
        url = self.base_url + path
        params = {
            'url': target_url,
            'comment': comment,
        }

        response = getattr(requests, 'post')(url,
                                             auth=self.oauth,
                                             headers=dict(),
                                             params=params)

        response.raise_for_status()

        return response.json()

    def get_bookmark(self, target_url):
        path = '/my/bookmark'
        url = self.base_url + path + "?url=" + target_url
        response = getattr(requests, 'get')(url,
                                            auth=self.oauth,
                                            headers=dict(),
                                            params=dict())
        response.raise_for_status()

        return response.json()