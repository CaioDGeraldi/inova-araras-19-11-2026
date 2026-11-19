from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from apps.discovery_routes.models import Route
from apps.establishments.forms import EstablishmentForm, ProductForm
from apps.establishments.models import Category, Establishment, Product


def home(request):
    query = request.GET.get("q", "").strip()
    category = request.GET.get("categoria", "")
    establishments = Establishment.objects.filter(status=Establishment.Status.APPROVED)
    if query:
        establishments = establishments.filter(
            Q(name__icontains=query) | Q(products__name__icontains=query, products__available=True)
        )
    if category.isdigit():
        establishments = establishments.filter(categories__id=category)
    return render(
        request,
        "home.html",
        {
            "establishments": establishments.distinct(),
            "routes": Route.objects.filter(published=True),
            "categories": Category.objects.all(),
            "query": query,
            "category": category,
        },
    )


def establishment_detail(request, slug):
    establishment = get_object_or_404(
        Establishment, slug=slug, status=Establishment.Status.APPROVED
    )
    return render(request, "establishments/detail.html", {"establishment": establishment})


@login_required
def panel(request):
    return render(
        request, "establishments/panel.html", {"establishments": request.user.establishments.all()}
    )


@login_required
def establishment_edit(request, slug):
    establishment = get_object_or_404(request.user.establishments, slug=slug)
    form = EstablishmentForm(request.POST or None, request.FILES or None, instance=establishment)
    if form.is_valid():
        form.save()
        return redirect("panel")
    return render(request, "establishments/form.html", {"form": form, "title": "Editar loja"})


@login_required
def product_edit(request, slug, pk=None):
    establishment = get_object_or_404(request.user.establishments, slug=slug)
    product = get_object_or_404(establishment.products, pk=pk) if pk else None
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)
    if form.is_valid():
        form.instance.establishment = establishment
        form.save()
        return redirect("panel")
    title = "Editar produto" if product else "Novo produto"
    return render(request, "establishments/form.html", {"form": form, "title": title})


@login_required
def product_delete(request, slug, pk):
    product = get_object_or_404(
        Product, pk=pk, establishment__slug=slug, establishment__owner=request.user
    )
    if request.method == "POST":
        product.delete()
        return redirect("panel")
    return render(request, "establishments/product_delete.html", {"product": product})
