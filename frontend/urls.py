from django.urls import path

from . import views

app_name = "frontend"
urlpatterns = [
    path('', views.index, name='index'),
    path('entries/<int:entry_id>', views.show, name='show')
]
