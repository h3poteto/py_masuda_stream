from django.shortcuts import render
from django.http import JsonResponse
from masuda.models.entry import Entry

def index(request):
    entries = Entry.objects.all()
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
            'posted_at': e.posted_at,
        })
    context = {
        'entries': array,
    }
    return JsonResponse(context)
