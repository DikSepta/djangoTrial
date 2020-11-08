# Create your models here.
import os
import sys
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

def upload_to(instance, filename):
    now = timezone.now()
    base, extension = os.path.splitext(filename.lower())
    return f"users/{instance.pk}/{now:%Y%m%d%H%M%S}{extension}"

class User(AbstractUser):
    # …
    robotMap = models.ImageField(_("Map"), upload_to=upload_to, blank=True)