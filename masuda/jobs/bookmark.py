from masuda.models.entry_detail import EntryDetail
from masuda.models.entry_bookmark import EntryBookmark
from datetime import datetime
from django.utils.timezone import get_current_timezone
import requests


# b.hatena.ne.jpからエントリーの詳細情報を持ってきて保存する
class Bookmark():
    api = 'http://b.hatena.ne.jp/entry/jsonlite/?url='

    def __init__(self, entry):
        self.entry = entry
        self.response = None

    def get(self):
        self.response = requests.get(
           Bookmark.api + self.entry.link,
        )

    def save(self):
        detail = self.__save_detail()
        self.__save_bookmarks(detail)

    def __save_detail(self):
        detail = EntryDetail.objects.create(
            entry=self.entry,
            eid=self.response.json()["eid"],
            count=self.response.json()["count"],
            url=self.response.json()["url"],
            title=self.response.json()["title"],
            screenshot=self.response.json()["screenshot"],
        )
        return detail

    def __save_bookmarks(self, detail):
        bookmarks = self.response.json()["bookmarks"]
        for b in bookmarks:
            EntryBookmark.objects.create(
                entry_detail=detail,
                bookmarked_at=get_current_timezone().localize(
                    datetime.strptime(
                        b["timestamp"],
                        '%Y/%m/%d %H:%M:%S')
                ),
                comment=b["comment"],
                user=b["user"],
            )
