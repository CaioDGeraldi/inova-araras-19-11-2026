from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from apps.campaigns.models import Coupon
from apps.core.forms import SignupForm
from apps.discovery_routes.models import Participation


def signup(request):
    form = SignupForm(request.POST or None)
    if form.is_valid():
        login(request, form.save())
        return redirect("home")
    return render(request, "registration/signup.html", {"form": form})


@login_required
def profile(request):
    return render(
        request,
        "core/profile.html",
        {
            "coupons": Coupon.objects.filter(consumer=request.user).select_related(
                "campaign__origin", "campaign__destination"
            ),
            "participations": Participation.objects.filter(user=request.user).select_related(
                "route"
            ),
        },
    )
