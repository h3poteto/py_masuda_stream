from django.conf.urls import url
from django.urls import path

from . import views

app_name = "frontend"
urlpatterns = [
    path('', views.index, name='index'),
    path('entries/<int:entry_id>', views.show, name='show'),
    path('bookmarks', views.index, name='bookmarks'),
    url(r"^accounts/password/change/$", views.not_found, name="account_change_password"),
    url(r"^accounts/password/set/$", views.not_found, name="account_set_password"),
    url(r"^accounts/inactive/$", views.not_found, name="account_inactive"),
    url(r"^accounts/email/$", views.not_found, name="account_email"),
    url(r"^accounts/confirm-email/$", views.not_found,
        name="account_email_verification_sent"),
    url(r"^accounts/confirm-email/(?P<key>[-:\w]+)/$", views.not_found,
        name="account_confirm_email"),
    url(r"^accounts/password/reset/$", views.not_found, name="account_reset_password"),
    url(r"^accounts/password/reset/done/$", views.not_found,
        name="account_reset_password_done"),
    url(r"^accounts/password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$", views.not_found,
        name="account_reset_password_from_key"),
    url(r"^accounts/password/reset/key/done/$", views.not_found,
        name="account_reset_password_from_key_done"),
]
