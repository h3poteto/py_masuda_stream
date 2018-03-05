from masuda.models.entry_detail import EntryDetail
from masuda.models.entry_bookmark import EntryBookmark
from datetime import datetime
from django.utils.timezone import get_current_timezone
import requests
from logging import getLogger


# b.hatena.ne.jpからエントリーの詳細情報を持ってきて保存する
class Bookmark():
    API = 'http://b.hatena.ne.jp/entry/jsonlite/?url='

    def __init__(self, entry, logger=None):
        self.entry = entry
        self.response = None
        self.json_body = None
        self.logger = logger or getLogger(__name__)

    def fetch(self):
        self.logger.info("Fetching bookmark: %s", self.entry.link)
        self.response = requests.get(
           self.API + self.entry.link,
        )
        self.json_body = self.response.json()

    def save(self):
        detail = self.__save_detail()
        self.__save_bookmarks(detail)
        self.logger.info("Save complete: %s", detail.id)

    def __save_detail(self):
        detail, created = EntryDetail.objects.update_or_create(
            entry=self.entry,
            defaults={
                'eid': self.json_body["eid"],
                'count': self.json_body["count"],
                'url': self.json_body["url"],
                'title': self.json_body["title"],
                'screenshot': self.json_body["screenshot"],
            },
        )
        return detail

    def __save_bookmarks(self, detail):
        bookmarks = self.json_body["bookmarks"]
        for b in bookmarks:
            timestamp = get_current_timezone().localize(
                datetime.strptime(
                    b["timestamp"],
                    '%Y/%m/%d %H:%M:%S')
            )
            # 厳密にやるならbookmarkは更新のたびに全て削除するのが望ましい
            # しかし，entry_detailとuserでuniqueにしてあるので，これをキーにしても問題ないだろう
            EntryBookmark.objects.update_or_create(
                entry_detail=detail,
                user=b["user"],
                defaults={
                    'bookmarked_at': timestamp,
                    'comment': b["comment"],
                },
            )
