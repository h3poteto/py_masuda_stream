from django.urls import path

from .views import user, bookmark

app_name = "user"
urlpatterns = [
    path('my', user.my, name="my"),
    path('bookmark', bookmark.Bookmark.as_view(), name="bookmark"),
]
