from django.http import JsonResponse
from django.utils import timezone
from datetime import datetime
from masuda.models.entry import Entry


def index(request):
    before = timezone.now()
    if "before" in request.GET:
        before = datetime.fromtimestamp(int(request.GET.get("before"))).replace(tzinfo=timezone.utc)
    entries = Entry.objects.filter(posted_at__lt=before).order_by('posted_at').reverse()[:20]
    array = []
    for e in entries:
        array.append({
            'id': e.id,
            'entry_id': e.entry_id,
            'title': e.title,
            'summary': e.summary,
            'content': e.content,
            'link': e.link,
            'hatena_bookmarkcount': e.hatena_bookmarkcount,
            'posted_at': e.posted_at.strftime("%s"),
        })
    context = {
        'entries': array,
    }
    return JsonResponse(context)


def show(request, entry_id):
    e = Entry.objects.select_related('entrydetail', 'anond').get(id=entry_id)
    entry = {
        'id': e.id,
        'entry_id': e.entry_id,
        'title': e.title,
        'summary': e.summary,
        'content': e.content,
        'anond_content_html': e.anond.content_html,
        'link': e.link,
        'hatena_bookmarkcount': e.entrydetail.count,
        'screenshot': e.entrydetail.screenshot,
        'posted_at': e.posted_at.strftime("%s"),
    }

    context = {
        'entry': entry,
    }
    return JsonResponse(context)


def bookmarks(request, entry_id):
    e = Entry.objects.select_related('entrydetail').prefetch_related('entrydetail__bookmarks').get(id=entry_id)
    bookmarks = []
    for b in e.entrydetail.bookmarks.all():
        bookmark = {
            'id': b.id,
            'comment': b.comment,
            'user': b.user,
            'bookmarked_at': b.bookmarked_at.strftime("%s"),
        }
        bookmarks.append(bookmark)

    context = {
        'bookmarks': bookmarks,
    }
    return JsonResponse(context)
