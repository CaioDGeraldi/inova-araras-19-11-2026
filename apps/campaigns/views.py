from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from apps.campaigns.models import Campaign, Coupon, Purchase
from apps.core.models import User
from apps.establishments.models import Establishment


@login_required
def purchase_confirm(request, code):
    consumer = get_object_or_404(User, account_code=code)
    establishments = request.user.establishments.filter(status=Establishment.Status.APPROVED)
    if not establishments:
        return render(request, "campaigns/not_owner.html", status=403)
    if request.method == "POST":
        establishment = get_object_or_404(establishments, pk=request.POST.get("establishment"))
        with transaction.atomic():
            purchase = Purchase.objects.create(
                establishment=establishment, consumer=consumer, confirmed_by=request.user
            )
            coupons = [
                Coupon.objects.create(campaign=campaign, consumer=consumer, purchase=purchase)
                for campaign in Campaign.objects.filter(
                    origin=establishment,
                    active=True,
                    destination__status=Establishment.Status.APPROVED,
                )
            ]
        return render(
            request,
            "campaigns/purchase_done.html",
            {"consumer": consumer, "establishment": establishment, "coupons": coupons},
        )
    return render(
        request,
        "campaigns/purchase_confirm.html",
        {"consumer": consumer, "establishments": establishments},
    )


@login_required
def coupon_redeem(request, code):
    coupon = get_object_or_404(
        Coupon.objects.select_related("campaign__destination", "campaign__origin", "consumer"),
        code=code,
    )
    if coupon.campaign.destination.owner_id != request.user.id:
        return render(request, "campaigns/not_owner.html", status=403)
    if request.method == "POST":
        with transaction.atomic():
            locked = get_object_or_404(
                Coupon.objects.select_for_update().select_related("campaign__destination"),
                code=code,
            )
            destination = locked.campaign.destination
            if (
                destination.owner_id != request.user.id
                or destination.status != Establishment.Status.APPROVED
            ):
                return render(request, "campaigns/not_owner.html", status=403)
            if locked.redeemed_at:
                messages.error(request, "Este cupom já foi resgatado.")
            else:
                locked.redeemed_at = timezone.now()
                locked.redeemed_by = request.user
                locked.save(update_fields=["redeemed_at", "redeemed_by"])
                messages.success(request, "Cupom resgatado.")
        return redirect("coupon_redeem", code=code)
    return render(request, "campaigns/coupon_redeem.html", {"coupon": coupon})
