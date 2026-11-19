from django.contrib import admin

from apps.campaigns.models import Campaign, Coupon, Purchase

admin.site.register(Campaign, list_display=["title", "origin", "destination", "active"])
admin.site.register(Purchase, list_display=["establishment", "consumer", "created_at"])
admin.site.register(Coupon, list_display=["campaign", "consumer", "created_at", "redeemed_at"])
