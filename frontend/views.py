from django.shortcuts import render
from django.http import Http404


def index(request):
    context = {}
    return render(request, 'frontend/index.html', context)


def show(request, entry_id):
    context = {}
    return render(request, 'frontend/index.html', context)


def not_found(request):
    # import pdb; pdb.set_trace()
    raise Http404
