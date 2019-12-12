# -*- coding: utf-8 -*-
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from import_export.admin import ImportExportModelAdmin

from .models import Category, Department, Vendor, Item


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'name', 'parent', 'stock_type')
    list_filter = ('parent', 'stock_type')
    search_fields = ('name',)


@admin.register(Department)
class DepartmentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Vendor)
class VendorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'website', 'email')
    search_fields = ('name',)


@admin.register(Item)
class ItemAdmin(ImportExportModelAdmin, SummernoteModelAdmin):
    summernote_fields = ('notes',)
    list_display = ('id', 'name', 'vendor', 'category', 'code', 'current_quantity', 'minimum',
                    'notes', 'price', 'date_expires')
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
