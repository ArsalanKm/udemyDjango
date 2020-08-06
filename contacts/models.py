from datetime import datetime

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from listings.models import Listing
from django.conf import settings


class Contact(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.name
