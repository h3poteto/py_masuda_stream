from django.urls import path

from .views import entries

urlpatterns = [
    path('entries', entries.index, name='index'),
]
