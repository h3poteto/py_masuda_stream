import requests
import xmltodict
from requests_oauthlib import OAuth1
from requests.exceptions import HTTPError


class HatenaAPIClient():
    rest_url = 'http://api.b.hatena.ne.jp/1'
    atom_url = 'http://b.hatena.ne.jp'

    def __init__(self, consumer_key, consumer_secret, oauth_token, oauth_token_secret):
        self.oauth = OAuth1(
            consumer_key,
            client_secret=consumer_secret,
            resource_owner_key=oauth_token,
            resource_owner_secret=oauth_token_secret)

    def add_bookmark(self, target_url, comment):
        path = '/my/bookmark'
        url = self.rest_url + path
        params = {
            'url': target_url,
            'comment': comment,
        }

        response = getattr(requests, 'post')(url,
                                             auth=self.oauth,
                                             headers=dict(),
                                             params=params)

        try:
            response.raise_for_status()
        except HTTPError as original:
            if response.status_code == 401:
                raise UnauthorizedError(*original.args) from original
            elif response.status_code == 404:
                raise NotFoundError(*original.args) from original

        return response.json()

    def get_bookmark(self, target_url):
        path = '/my/bookmark'
        url = self.rest_url + path + "?url=" + target_url
        response = getattr(requests, 'get')(url,
                                            auth=self.oauth,
                                            headers=dict(),
                                            params=dict())
        try:
            response.raise_for_status()
        except HTTPError as original:
            if response.status_code == 401:
                raise UnauthorizedError(*original.args) from original
            elif response.status_code == 404:
                raise NotFoundError(*original.args) from original

        return response.json()

    def bookmarks(self):
        # http://developer.hatena.ne.jp/ja/documents/bookmark/apis/atom
        path = '/atom/feed'
        url = self.atom_url + path
        response = getattr(requests, 'get')(url,
                                            auth=self.oauth,
                                            headers=dict(),
                                            params=dict())
        # import pdb; pdb.set_trace()
        try:
            response.raise_for_status()
        except HTTPError as original:
            if response.status_code == 401:
                raise UnauthorizedError(*original.args) from original
            elif response.status_code == 404:
                raise NotFoundError(*original.args) from original

        return xmltodict.parse(response.text)


class UnauthorizedError(HTTPError):
    pass


class NotFoundError(HTTPError):
    pass
