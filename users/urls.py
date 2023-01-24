from . import views
from django.urls import path

urlpatterns = [
    path("index/", views.index, name="dashboard"),
    path("withdraw-funds/", views.withdraw, name="withdraw"),
    path("transactions/", views.transactions_, name="transactions"),
    path("account-settings/", views.settings, name="settings"),
    # path("password-settings/", views.change_password, name="change_password"),
]
