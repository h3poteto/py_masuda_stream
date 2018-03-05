from pyquery import PyQuery
from urllib.parse import urlparse
from logging import getLogger
from masuda.models.entry import Entry
import masuda.models.anond


# anond.hatelabo.jpの特定記事をスクレイピングし内容を保存する
# ここはAPIを提供していないのでスクレイピングするしかない
class Anond():
    Host = "anond.hatelabo.jp"

    def __init__(self, entry, logger=None):
        if isinstance(entry, Entry) is not True:
            raise TypeError('entry is not Entry')

        self.entry = entry
        self.content_html = ""
        self.logger = logger or getLogger(__name__)

    # entryのURLから記事の中身を取ってくる
    def fetch(self):
        # anondかどうかのチェック
        url = urlparse(self.entry.link)
        if url.hostname != self.Host:
            raise RuntimeError(self.Host)

        self.logger.info("Fetching anond: %s", self.entry.link)
        pq = PyQuery(url=self.entry.link)
        elements = []
        content_start = False
        # make_links_absoluteではてなキーワードへのリンクを相対パスから絶対URLに変更しておく必要がある
        for element in pq.find("div.section").make_links_absolute().children():
            # #title-below-text-adから#rectangle-middleまでのhtmlをまるごといただく
            if pq(element).attr.id == "rectangle-middle":
                content_start = False

            if content_start:
                elements.append(pq(element).outerHtml())

            if pq(element).attr.id == "title-below-text-ad":
                content_start = True

        self.content_html = ''.join(elements)

    def save(self):
        # 保存済みだった場合には情報を更新する
        o, created = masuda.models.anond.Anond.objects.update_or_create(
            entry=self.entry,
            defaults={
                'content_html': self.content_html,
            },
        )
        self.logger.info("Save complete: %s", o.id)
