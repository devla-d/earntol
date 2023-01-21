from . import views
from django.urls import path

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("about/", views.about, name="about"),
    path("pricing/", views.pricing, name="pricing"),
    path("support/", views.support, name="support"),
]
