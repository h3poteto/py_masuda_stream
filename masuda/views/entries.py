from django.shortcuts import render

from masuda.models.entries import Entry

def index(request):
    entries = Entry.objects.all()
    context = {
        'entries': entries,
    }
    return render(request, 'masuda/entries/index.html', context)
