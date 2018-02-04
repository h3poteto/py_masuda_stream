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
