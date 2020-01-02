# -*- coding: utf-8 -*-
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from import_export.admin import ImportExportModelAdmin
from django.utils.safestring import mark_safe
from adminsortable.admin import SortableAdmin
from django.forms import ModelForm
from django import forms
# from django.db.models import BooleanField, CharField

from .models import Category, Vendor, Item


class SwitchWidget(forms.Widget):
    template_name = 'switch.html'


class BaseAdminForm(ModelForm):
    active = forms.BooleanField(required=False, widget=SwitchWidget(
        attrs={"help": "Turn off to no longer use this item rather than deleting it."}))


class BaseAdminListForm(ModelForm):
    active = forms.BooleanField(
        required=False, widget=SwitchWidget(attrs={"extra_class": "small"}))


class BaseAdmin(SortableAdmin, ImportExportModelAdmin):
    change_list_template_extends = 'admin/change_list_sortable.html'
    list_display_links = ['name']
    list_editable = ('active',)
    list_display = ('active', 'name')
    form = BaseAdminForm
    save_as = True

    def get_changelist_form(self, request, **kwargs):
        kwargs.setdefault('form', BaseAdminListForm)
        return super(BaseAdmin, self).get_changelist_form(request, **kwargs)


@admin.register(Category)
class CategoryAdmin(BaseAdmin):
    list_display = BaseAdmin.list_display + ('parent', 'stock_type')
    list_filter = ('parent', 'stock_type')
    search_fields = ('name',)


@admin.register(Vendor)
class VendorAdmin(BaseAdmin):
    list_display = BaseAdmin.list_display + ('address', 'website', 'email')
    search_fields = ('name',)


@admin.register(Item)
class ItemAdmin(BaseAdmin, SummernoteModelAdmin):
    summernote_fields = ('notes',)
    list_display = BaseAdmin.list_display + (
        'vendor', 'category', 'code', 'current_quantity', 'minimum', 'rendered_notes',
        'price')
    list_display_links = ['name', 'rendered_notes']
    list_filter = ('vendor', 'category', 'date_added', 'date_modified')
    search_fields = ('name',)
    fieldsets = [
        (None, {
            'fields': [
                'active', 'name', 'code', 'price',
                'vendor', 'category',
                'current_quantity', 'minimum',
                'date_expires',
                'notes'
            ]
        })
    ]

    # Adds a custom field to show the item's notes as rendered html.
    def rendered_notes(self, instance):
        return mark_safe(instance.notes)

    # Changes column label name from "Rendered Notes" to just "Notes"
    rendered_notes.short_description = "Notes"
