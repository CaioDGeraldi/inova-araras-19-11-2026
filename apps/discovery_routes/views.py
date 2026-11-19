from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from apps.discovery_routes.models import Participation, Route, Stop


def route_list(request):
    return render(
        request, "discovery_routes/list.html", {"routes": Route.objects.filter(published=True)}
    )


def route_detail(request, slug):
    route = get_object_or_404(Route, slug=slug, published=True)
    participation = None
    visited = set()
    if request.user.is_authenticated:
        participation = Participation.objects.filter(user=request.user, route=route).first()
        visited = participation.visited_stop_ids() if participation else set()
    stops = route.stops.select_related("establishment", "event")
    return render(
        request,
        "discovery_routes/detail.html",
        {
            "route": route,
            "stops": stops,
            "participation": participation,
            "visited": visited,
            "visited_count": len(visited),
            "total": len(stops),
        },
    )


@login_required
def checkin(request, token):
    stop = get_object_or_404(
        Stop.objects.select_related("route"), token=token, route__published=True
    )
    period_error = stop.route.period_error()
    if period_error:
        messages.error(request, f"Check-in recusado. {period_error}")
        return redirect(stop.route)
    participation, _ = Participation.objects.get_or_create(user=request.user, route=stop.route)
    participation.check_in(stop)
    return render(
        request, "discovery_routes/checkin.html", {"stop": stop, "participation": participation}
    )


@staff_member_required
def route_qr(request, slug):
    route = get_object_or_404(Route, slug=slug)
    return render(request, "discovery_routes/qr.html", {"route": route, "stops": route.stops.all()})
