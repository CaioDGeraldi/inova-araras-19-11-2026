from django.contrib import admin

from apps.events.models import Event

admin.site.register(Event, list_display=["title", "starts_at", "status"], list_filter=["status"])
