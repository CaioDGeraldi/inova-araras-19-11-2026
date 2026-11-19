from django.shortcuts import get_object_or_404, render

from apps.events.models import Event


def event_list(request):
    return render(request, "events/list.html", {"events": Event.objects.all()})


def event_detail(request, pk):
    return render(request, "events/detail.html", {"event": get_object_or_404(Event, pk=pk)})
