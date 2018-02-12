from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('entries/<int:entry_id>', views.show, name='show')
]
