from django.db.models import (
    Model, CharField, IntegerField, ForeignKey, TextField, ForeignKey, ManyToManyField,
    DateField, SET_NULL)

from smokestack.users.models import User


# Create your models here.
class Tasks(Model):
    title = TextField(blank=False, null=False)
    assigned_to = ForeignKey(User, on_delete=SET_NULL, null=True)
    assigned_by = ForeignKey(User, on_delete=SET_NULL, related_name="delegated_tasks", null=True)
    date_due = DateField(blank=False, null=False)
    priority = IntegerField(default=0)
    order = IntegerField(default=0)
    points = IntegerField(default=0)


class TaskCategory(Model):
    title = TextField(blank=False, null=False)
    tasks = ManyToManyField(Tasks)
    order = IntegerField(default=0)
