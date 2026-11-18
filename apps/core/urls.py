from django.urls import path

from apps.core.api import healthcheck

urlpatterns = [
    path("health/", healthcheck, name="healthcheck"),
]
