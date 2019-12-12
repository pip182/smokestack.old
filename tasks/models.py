from django.db.models import (
    Model, CharField, IntegerField, TextField, ForeignKey, ManyToManyField, DateField,
    SET_NULL)

from smokestack.users.models import User


# Create your models here.
class Tasks(Model):
    title = TextField(default="", blank=False, null=False)
    assigned_to = ForeignKey(User, on_delete=SET_NULL, null=True)
    assigned_by = ForeignKey(User, on_delete=SET_NULL, related_name="delegated_tasks", null=True)
    date_due = DateField(blank=False, null=False)
