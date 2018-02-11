from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'frontend/index.html', context)


def show(request, entry_id):
    context = {}
    return render(request, 'frontend/index.html', context)
