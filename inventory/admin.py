# -*- coding: utf-8 -*-
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from import_export.admin import ImportExportModelAdmin
from django.utils.safestring import mark_safe
from adminsortable2.admin import SortableAdminMixin

from .models import Category, Department, Vendor, Item


@admin.register(Category)
class CategoryAdmin(SortableAdminMixin, ImportExportModelAdmin):
    list_display = ('order', 'name', 'parent', 'stock_type')
    list_filter = ('parent', 'stock_type')
    search_fields = ('name',)


@admin.register(Department)
class DepartmentAdmin(SortableAdminMixin, ImportExportModelAdmin):
    list_display = ('order', 'name')
    search_fields = ('name',)


@admin.register(Vendor)
class VendorAdmin(SortableAdminMixin, ImportExportModelAdmin):
    list_display = ('order', 'name', 'address', 'website', 'email')
    search_fields = ('name',)


@admin.register(Item)
class ItemAdmin(SortableAdminMixin, ImportExportModelAdmin, SummernoteModelAdmin):
    summernote_fields = ('notes',)
    list_display = ('order', 'name', 'vendor', 'category', 'code', 'current_quantity',
                    'minimum', 'rendered_notes', 'price')
    list_display_links = ['name', 'rendered_notes']
    list_filter = ('vendor', 'category', 'date_added', 'date_modified')
    search_fields = ('name',)
    fieldsets = [
        (None, {
            'fields': [
                'name', 'code', 'price',
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
