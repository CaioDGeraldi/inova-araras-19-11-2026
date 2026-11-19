import secrets

from django.conf import settings
from django.db import models

from apps.establishments.models import Establishment


def new_coupon_code():
    return secrets.token_urlsafe(12)


class Campaign(models.Model):
    title = models.CharField("título", max_length=150)
    benefit = models.CharField("benefício", max_length=200)
    origin = models.ForeignKey(
        Establishment,
        on_delete=models.PROTECT,
        related_name="issued_campaigns",
        verbose_name="loja de origem",
    )
    destination = models.ForeignKey(
        Establishment,
        on_delete=models.PROTECT,
        related_name="received_campaigns",
        verbose_name="loja receptora",
    )
    active = models.BooleanField("ativa", default=True)

    class Meta:
        verbose_name = "campanha"

    def __str__(self):
        return self.title


class Purchase(models.Model):
    establishment = models.ForeignKey(Establishment, on_delete=models.PROTECT)
    consumer = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="purchases"
    )
    confirmed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="+"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "compra confirmada"
        verbose_name_plural = "compras confirmadas"


class Coupon(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.PROTECT, related_name="coupons")
    consumer = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="coupons"
    )
    purchase = models.ForeignKey(Purchase, on_delete=models.PROTECT, related_name="coupons")
    code = models.CharField(max_length=32, unique=True, default=new_coupon_code, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    redeemed_at = models.DateTimeField(null=True, blank=True)
    redeemed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=True, blank=True, related_name="+"
    )

    class Meta:
        verbose_name = "cupom"
