from django.db.models import (
    Model, CharField, PositiveIntegerField, DecimalField, IntegerField, DateField,
    ForeignKey, TextField, BooleanField, SET_NULL, CASCADE)
from smokestack.users.models import User, Customer
from adminsortable.models import SortableMixin, Sortable


class BaseModel(SortableMixin):
    active = BooleanField(default=True, help_text="Turn off to no longer have the item available rather than deleting it.")
    name = CharField(max_length=200)
    position = PositiveIntegerField(default=0, editable=False, db_index=True)

    def __str__(self):
        return self.name

    @property
    def next_position(self):
        self.position = max([i.position for i in self.__class__.objects.all()]) + 1
        return self.position

    class Meta:
        abstract = True
        ordering = ['position']

    def barcode(self):
        name = self.__class__.__name__
        return "{}{}{}".format(name[:2], name[-2:], self.id)


class Project(BaseModel):
    # Project type constants. Can be referenced by doing Project.STANDARD for example
    STANDARD = 1
    HOTLIST = 2
    SAMPLE = 3

    customer = ForeignKey(Customer, on_delete=CASCADE)
    date_added = DateField(auto_now_add=True)
    date_ships = DateField(blank=True, null=True)
    delivery_address = TextField(blank=True, null=True)
    value = DecimalField(decimal_places=2, max_digits=20)
    project_type = IntegerField(default=0, choices=[
        (STANDARD, 'Standard'),
        (HOTLIST, 'Hot List'),
        (SAMPLE, 'Sample'),
    ])


class ProjectPhase(BaseModel):
    project = ForeignKey(Project, on_delete=CASCADE)


class Department(BaseModel):
    pass


class DepartmentWork(BaseModel):
    department = ForeignKey(Department, on_delete=CASCADE)
    phase = ForeignKey(ProjectPhase, on_delete=CASCADE)
