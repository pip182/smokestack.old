from django.contrib import admin
# from django_summernote.admin import SummernoteModelAdmin
from import_export.admin import ImportExportModelAdmin
# from django.utils.safestring import mark_safe
from adminsortable.admin import SortableAdmin

from .models import Department


@admin.register(Department)
class DepartmentAdmin(SortableAdmin, ImportExportModelAdmin):
    list_display = ('position', 'name')
    search_fields = ('name',)
