import feedparser
from concurrent.futures import ThreadPoolExecutor
import logging
from masuda.models.entry import Entry
from masuda.jobs.anond import Anond
from masuda.jobs.bookmark import Bookmark


# $ python manage.py runscript masuda.rss
# https://syncer.jp/hatebu-api-matome

HATENA_DOMAIN = "http://b.hatena.ne.jp"
ANOND_URL = "https%3A%2F%2Fanond.hatelabo.jp%2F"


def run():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.info("Fetching...")

    rss_url = HATENA_DOMAIN + "/entrylist?mode=rss" + "&url=" + ANOND_URL + "&sort=recent"
    rss = feedparser.parse(rss_url)
    logger.debug(rss.entries[0].keys())
    entries = []
    for e in rss.entries:
        # entryが保存済みであった場合には，情報を更新したい
        entry, created = Entry.objects.update_or_create(
            entry_id=e.id,
            defaults={
                'title': e.title,
                'summary': e.summary,
                'content': e.content,
                'link': e.link,
                'hatena_bookmarkcount': e.hatena_bookmarkcount,
                'posted_at': e.updated,
            },
        )
        entries.append(entry)
        logger.info("Save complete: %s", entry.id)

    # 保存されたentry情報に基づいてanondとbookmarkの情報を更新する
    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(async_anond, entries, logger)
        executor.submit(async_bookmark, entries, logger)


def async_anond(entries=[], logger=None):
    for e in entries:
        anond = Anond(e, logger)
        anond.fetch()
        anond.save()


def async_bookmark(entries=[], logger=None):
    for e in entries:
        b = Bookmark(e, logger)
        b.fetch()
        b.save()
