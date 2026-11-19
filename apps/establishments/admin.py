from django.contrib import admin

from apps.establishments.models import Category, Establishment, Product


@admin.register(Establishment)
class EstablishmentAdmin(admin.ModelAdmin):
    list_display = ["name", "owner", "status"]
    list_filter = ["status"]
    prepopulated_fields = {"slug": ["name"]}
    actions = ["approve", "reject", "suspend"]

    def _set_status(self, request, queryset, status):
        updated = queryset.update(status=status)
        self.message_user(request, f"{updated} loja(s) atualizada(s) para {status}.")

    @admin.action(description="Aprovar lojas selecionadas")
    def approve(self, request, queryset):
        self._set_status(request, queryset, Establishment.Status.APPROVED)

    @admin.action(description="Rejeitar lojas selecionadas")
    def reject(self, request, queryset):
        self._set_status(request, queryset, Establishment.Status.REJECTED)

    @admin.action(description="Suspender lojas selecionadas")
    def suspend(self, request, queryset):
        self._set_status(request, queryset, Establishment.Status.SUSPENDED)


admin.site.register(Category)
admin.site.register(Product, list_display=["name", "establishment", "price", "available"])
