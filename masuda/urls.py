from django.urls import path

from .views import entries

urlpatterns = [
    path('', entries.index, name='index'),
]
