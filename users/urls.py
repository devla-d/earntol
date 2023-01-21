from . import views
from django.urls import path

urlpatterns = [
    path("index/", views.index, name="dashboard"),
    path("withdraw-funds/", views.withdraw, name="withdraw"),
    path("transactions/", views.transactions_, name="transactions"),
]
