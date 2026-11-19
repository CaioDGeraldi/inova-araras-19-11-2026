from django.db import models
from django.urls import reverse

from apps.establishments.models import Establishment


class Event(models.Model):
    class Status(models.TextChoices):
        PUBLISHED = "publicado", "Publicado"
        CANCELLED = "cancelado", "Cancelado"

    title = models.CharField("título", max_length=150)
    description = models.TextField("descrição", blank=True)
    starts_at = models.DateTimeField("início")
    ends_at = models.DateTimeField("fim")
    location = models.CharField("local", max_length=200)
    category = models.CharField("categoria", max_length=80, blank=True)
    organizer = models.CharField("organizador", max_length=150)
    free = models.BooleanField("gratuito", default=True)
    requires_registration = models.BooleanField("exige inscrição", default=False)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.PUBLISHED)
    establishment = models.ForeignKey(
        Establishment, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="loja"
    )

    class Meta:
        ordering = ["starts_at"]
        verbose_name = "evento"

    def __str__(self):
        return self.title

    @property
    def cancelled(self):
        return self.status == self.Status.CANCELLED

    def get_absolute_url(self):
        return reverse("event_detail", args=[self.pk])
