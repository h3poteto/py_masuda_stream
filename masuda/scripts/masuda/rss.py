import feedparser
from masuda.models.entry import Entry
from django.db.utils import IntegrityError


# $ python manage.py runscript masuda.rss
# https://syncer.jp/hatebu-api-matome

HATENA_DOMAIN = "http://b.hatena.ne.jp"
ANOND_URL = "https%3A%2F%2Fanond.hatelabo.jp%2F"


def run():
    rss_url = HATENA_DOMAIN + "/entrylist?mode=rss" + "&url=" + ANOND_URL + "&sort=recent"
    rss = feedparser.parse(rss_url)
    print(rss.entries[0].keys())
    for e in rss.entries:
        entry = Entry(
            entry_id=e.id,
            title=e.title,
            summary=e.summary,
            content=e.content,
            link=e.link,
            hatena_bookmarkcount=e.hatena_bookmarkcount,
            posted_at=e.updated,
        )
        try:
            entry.save()
        except IntegrityError:
            print("Save error: %s" % entry.__dict__.values())
