from urllib.parse import quote

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from PIL import Image, UnidentifiedImageError

IMAGE_FORMATS = {"JPEG", "PNG", "WEBP"}
IMAGE_MAX_BYTES = 5 * 1024 * 1024


def validate_image(file):
    if file.size > IMAGE_MAX_BYTES:
        raise ValidationError("A imagem deve ter no máximo 5 MB.")
    file.seek(0)
    try:
        image_format = Image.open(file).format
    except (UnidentifiedImageError, OSError):
        image_format = None
    finally:
        file.seek(0)
    if image_format not in IMAGE_FORMATS:
        raise ValidationError("Envie uma imagem JPEG, PNG ou WebP.")


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
        REJECTED = "rejeitado", "Rejeitado"
        SUSPENDED = "suspenso", "Suspenso"

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="establishments"
    )
    name = models.CharField("nome", max_length=120)
    slug = models.SlugField(unique=True)
    description = models.TextField("descrição", blank=True)
    image = models.ImageField("imagem", upload_to="lojas/", blank=True, validators=[validate_image])
    postal_code = models.CharField("CEP", max_length=9, blank=True)
    street = models.CharField("logradouro", max_length=200, blank=True)
    number = models.CharField("número", max_length=20, blank=True)
    district = models.CharField("bairro", max_length=80, blank=True)
    city = models.CharField("município", max_length=80, blank=True)
    state = models.CharField("UF", max_length=2, blank=True)
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

    def full_address(self):
        street = ", ".join(part for part in [self.street, self.number] if part)
        city = "/".join(part for part in [self.city, self.state] if part)
        place = " - ".join(part for part in [self.district, city] if part)
        return ", ".join(part for part in [street, place, self.postal_code] if part)

    def directions_url(self):
        address = self.full_address()
        if not address:
            return ""
        return f"https://www.google.com/maps/search/?api=1&query={quote(address)}"

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
    image = models.ImageField(
        "imagem", upload_to="produtos/", blank=True, validators=[validate_image]
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "produto"

    def __str__(self):
        return self.name
