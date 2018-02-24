from django.urls import path

from . import views

app_name = "user"
urlpatterns = [
    path('my', views.my, name="my"),
]
