import secrets

from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone

from apps.establishments.models import Establishment
from apps.events.models import Event


def new_stop_token():
    return secrets.token_urlsafe(12)


class Route(models.Model):
    title = models.CharField("título", max_length=150)
    slug = models.SlugField(unique=True)
    description = models.TextField("descrição", blank=True)
    published = models.BooleanField("publicada", default=True)
    starts_on = models.DateField("início", null=True, blank=True)
    ends_on = models.DateField("fim", null=True, blank=True)

    class Meta:
        ordering = ["title"]
        verbose_name = "rota"

    def __str__(self):
        return self.title

    def period_error(self):
        today = timezone.localdate()
        if self.starts_on and today < self.starts_on:
            return f"A rota começa em {self.starts_on:%d/%m/%Y}."
        if self.ends_on and today > self.ends_on:
            return f"A rota terminou em {self.ends_on:%d/%m/%Y}."
        return ""

    def get_absolute_url(self):
        return reverse("route_detail", args=[self.slug])


class Stop(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE, related_name="stops")
    name = models.CharField("nome", max_length=150)
    establishment = models.ForeignKey(
        Establishment,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        verbose_name="estabelecimento",
    )
    event = models.ForeignKey(
        Event,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="stops",
        verbose_name="evento",
    )
    order = models.PositiveSmallIntegerField("ordem", default=0)
    required = models.BooleanField("obrigatória", default=True)
    token = models.CharField(max_length=32, unique=True, default=new_stop_token, editable=False)

    class Meta:
        ordering = ["route", "order"]
        verbose_name = "parada"

    def __str__(self):
        return f"{self.route} · {self.name}"


class Participation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    started_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["user", "route"], name="one_participation_per_route")
        ]
        verbose_name = "participação"

    def visited_stop_ids(self):
        return set(self.checkins.values_list("stop_id", flat=True))

    def check_in(self, stop):
        self.checkins.get_or_create(stop=stop)
        required = set(self.route.stops.filter(required=True).values_list("id", flat=True))
        if not self.completed_at and required <= self.visited_stop_ids():
            self.completed_at = timezone.now()
            self.save(update_fields=["completed_at"])


class CheckIn(models.Model):
    participation = models.ForeignKey(
        Participation, on_delete=models.CASCADE, related_name="checkins"
    )
    stop = models.ForeignKey(Stop, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["participation", "stop"], name="one_checkin_per_stop")
        ]
        verbose_name = "check-in"
