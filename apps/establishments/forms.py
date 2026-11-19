from django import forms

from apps.establishments.models import Establishment, Product


class EstablishmentForm(forms.ModelForm):
    class Meta:
        model = Establishment
        fields = ["name", "description", "address", "whatsapp", "instagram", "categories"]
        widgets = {"categories": forms.CheckboxSelectMultiple}


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "price", "available"]
