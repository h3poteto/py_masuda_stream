from pyquery import PyQuery
from urllib.parse import urlparse
from masuda.models.entry import Entry
import masuda.models.anond.Anond


# anond.hatelabo.jpの特定記事をスクレイピングし内容を保存する
# ここはAPIを提供していないのでスクレイピングするしかない
class Anond():
    host = "anond.hatelabo.jp"

    def __init__(self, entry):
        if isinstance(entry, Entry) is not True:
            raise TypeError('entry is not Entry')

        self.entry = entry
        self.content_html = ""

    # entryのURLから記事の中身を取ってくる
    def fetch(self):
        # anondかどうかのチェック
        url = urlparse(self.entry.link)
        if url.hostname != Anond.host:
            raise RuntimeError(Anond.host)

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
        masuda.models.anond.Anond.objects.create(
            entry=self.entry,
            content_html=self.content_html,
        )
