from django.db.models import (
    Model, CharField, IntegerField, TextField, ForeignKey, ManyToManyField, DateField,
    DateTimeField, DecimalField,  BooleanField, PositiveIntegerField, SET_NULL)
from djmoney.models.fields import MoneyField
from smokestack.models import BaseModel, Department
from datetime import datetime
from adminsortable.fields import SortableForeignKey


HARDWARE = 1
SHEET = 2
HARDWOOD = 3
EDGEBANDING = 4
MISC = 5


class Category(BaseModel):
    parent = ForeignKey('self', null=True, blank=True, on_delete=SET_NULL)
    stock_type = IntegerField(default=0, choices=[
        (HARDWARE, 'Hardware'),
        (SHEET, 'Sheet'),
        (HARDWOOD, 'Hardwood'),
        (EDGEBANDING, 'Edgebanding'),
        (MISC, 'Miscellaneous')
    ])

    def get_items(self):
        cat = self
        category_ids = [cat.id]
        while cat.has_parent:
            cat = cat.parent
            category_ids.append(cat.id)
        return Item.objects.filter(category__in=category_ids)

    @property
    def get_xpath(self):
        cat = self
        items = [cat.name]
        while cat.has_parent:
            cat = cat.parent
            items.append(cat.name)
        if len(items) > 1:
            return " -> ".join([i for i in reversed(items)])
        else:
            return items[0]

    @property
    def has_parent(self):
        return True if self.parent else False

    @property
    def parent_count(self):
        cat = self
        count = 0
        while cat.has_parent:
            cat = cat.parent
            count += 1
        return count

    @property
    def item_count(self):
        return len(self.get_items())

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['position']


class Vendor(BaseModel):
    address = TextField(null=True)
    website = CharField(max_length=200, null=True)
    email = CharField(max_length=200, null=True)


class Item(BaseModel):
    vendor = ForeignKey(Vendor, null=True, blank=True, on_delete=SET_NULL)
    category = SortableForeignKey(Category, null=True, blank=True, on_delete=SET_NULL)
    code = CharField(max_length=200, null=True, blank=True)
    current_quantity = IntegerField(default=0)
    minimum = IntegerField(default=0)
    notes = TextField(default="", blank=True)
    price = DecimalField(max_digits=10, decimal_places=2)
    date_added = DateField(auto_now_add=True)
    date_modified = DateField(auto_now=True)
    date_expires = DateField(blank=True, null=True)


class Event(Model):
    department = ForeignKey(Department, null=True, on_delete=SET_NULL)
    item = ForeignKey(Item, null=True, on_delete=SET_NULL)
    timestamp = DateTimeField(default=datetime.now)
    qty = IntegerField(null=True)
