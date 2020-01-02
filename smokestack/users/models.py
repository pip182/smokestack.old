from django.contrib.auth.models import AbstractUser
from django.db.models import (
    Model, CharField, IntegerField, BooleanField, TextField, ForeignKey, SET_NULL)

from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):

    # First Name and Last Name do not cover name patterns around the globe.
    name = CharField(_("Name of User"), blank=True, max_length=255)
    address = TextField(blank=True)
    phone = CharField(max_length=11, blank=True)
    email = CharField(max_length=200, blank=True)
    task_points = IntegerField(blank=True, null=True)
    shop_staff = BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})


class Customer(Model):
    user_account = ForeignKey(User, null=True, on_delete=SET_NULL)
    name = CharField(_("Dealer Name"), max_length=200)
    address = TextField(blank=True)
    phone = CharField(max_length=11, blank=True)
    email = CharField(max_length=200, blank=True)
