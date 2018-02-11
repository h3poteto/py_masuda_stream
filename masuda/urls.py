from django.urls import path

from .views import entries

app_name = 'masuda'
urlpatterns = [
    path('entries', entries.index, name='index'),
    path('entries/<int:entry_id>', entries.show, name='show'),
    path('entries/<int:entry_id>/bookmarks', entries.bookmarks, name='bookmarks')
]
