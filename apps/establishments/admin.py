from django.contrib import admin

from apps.establishments.models import Category, Establishment, Product

admin.site.register(Category)
admin.site.register(Product, list_display=["name", "establishment", "price", "available"])
admin.site.register(
    Establishment,
    list_display=["name", "owner", "status"],
    list_filter=["status"],
    prepopulated_fields={"slug": ["name"]},
)
