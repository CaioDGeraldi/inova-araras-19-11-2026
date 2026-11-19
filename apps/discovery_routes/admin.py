from django.contrib import admin

from apps.discovery_routes.models import CheckIn, Participation, Route, Stop


class StopInline(admin.TabularInline):
    model = Stop
    readonly_fields = ["token"]


admin.site.register(
    Route,
    inlines=[StopInline],
    list_display=["title", "published"],
    prepopulated_fields={"slug": ["title"]},
)
admin.site.register(Participation, list_display=["route", "user", "started_at", "completed_at"])
admin.site.register(CheckIn, list_display=["participation", "stop", "created_at"])
