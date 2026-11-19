import secrets
import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


def new_account_code():
    return secrets.token_urlsafe(12)


class User(AbstractUser):
    # shortcut: código estático por conta, trocar por token temporário da Spec 007
    account_code = models.CharField(max_length=32, unique=True, default=new_account_code)


class UUIDModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
