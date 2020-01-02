from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import (
    Model, CharField, IntegerField, TextField, ForeignKey, ManyToManyField, DateField,
    PositiveSmallIntegerField, SET_NULL, CASCADE)

from smokestack.users.models import User


# Status Constants
STATUS_NEW = 0
STATUS_IN_PROGRESS = 1
STATUS_ON_HOLD = 2
STATUS_COMPLETED = 3


class TaskComments(Model):
    date_added = DateField(auto_now_add=True)
    name = ForeignKey(User, related_name='task_comments', on_delete=CASCADE)
    sub_comments = ManyToManyField('self')
    text = TextField

    class Meta:
        verbose_name_plural = "Task Comments"


class Task(Model):
    assigned_by = ForeignKey(User, on_delete=SET_NULL, blank=True, null=True, related_name="delegated")
    assigned_to = ForeignKey(User, on_delete=SET_NULL, blank=True, null=True)
    date_due = DateField(blank=True, null=True)
    position = IntegerField(default=0)
    points = IntegerField(default=0)
    priority = IntegerField(default=0)
    status = IntegerField(default=0, choices=[
        (STATUS_NEW, 'New'),
        (STATUS_IN_PROGRESS, 'In Progress'),
        (STATUS_ON_HOLD, 'On Hold'),
        (STATUS_COMPLETED, 'Completed'),
    ])
    sub_tasks = ManyToManyField('self', blank=True)
    title = CharField(max_length=200, blank=False, null=False)

    _progress = PositiveSmallIntegerField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])

    @property
    def progress(self):
        if self.sub_tasks.count():
            sub_points = [float(t.points) for t in self.sub_tasks.all()]
            return int(round((sum(sub_points) / float(self.points)) * 100))
        else:
            return self._progress


class TaskCategory(Model):
    position = IntegerField(default=0)
    tasks = ManyToManyField(Task)
    title = TextField(blank=False, null=False)

    class Meta:
        verbose_name_plural = "Task Categories"
