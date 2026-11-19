from urllib.parse import quote

from django.conf import settings
from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField("nome", max_length=80, unique=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "categoria"

    def __str__(self):
        return self.name


class Establishment(models.Model):
    class Status(models.TextChoices):
        PENDING = "pendente", "Pendente"
        APPROVED = "aprovado", "Aprovado"

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="establishments"
    )
    name = models.CharField("nome", max_length=120)
    slug = models.SlugField(unique=True)
    description = models.TextField("descrição", blank=True)
    address = models.CharField("endereço", max_length=200, blank=True)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.PENDING)
    whatsapp = models.CharField("WhatsApp (só números, com DDD)", max_length=20, blank=True)
    instagram = models.CharField("Instagram (usuário)", max_length=60, blank=True)
    categories = models.ManyToManyField(
        Category, blank=True, related_name="establishments", verbose_name="categorias"
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "estabelecimento"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("establishment_detail", args=[self.slug])

    def whatsapp_url(self):
        digits = "".join(c for c in self.whatsapp if c.isdigit())
        if not digits:
            return ""
        text = quote(f"Olá, {self.name}! Vi a loja no Vem pro Centro e quero reservar um produto.")
        return f"https://wa.me/55{digits}?text={text}"

    def instagram_url(self):
        return f"https://instagram.com/{self.instagram.lstrip('@')}" if self.instagram else ""


class Product(models.Model):
    establishment = models.ForeignKey(
        Establishment, on_delete=models.CASCADE, related_name="products", verbose_name="loja"
    )
    name = models.CharField("nome", max_length=120)
    description = models.TextField("descrição", blank=True)
    price = models.DecimalField("preço", max_digits=9, decimal_places=2, null=True, blank=True)
    available = models.BooleanField("disponível", default=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "produto"

    def __str__(self):
        return self.name
