from django.shortcuts import get_object_or_404, render

from apps.discovery_routes.models import Route
from apps.events.models import Event


def event_list(request):
    return render(request, "events/list.html", {"events": Event.objects.all()})


def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    routes = Route.objects.filter(published=True, stops__event=event).distinct()
    return render(request, "events/detail.html", {"event": event, "routes": routes})
