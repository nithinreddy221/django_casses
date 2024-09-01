from django.contrib import admin
from .models import Departments


# Register your models here.

class DepartmentsAdmin(admin.ModelAdmin):
    list_display = ('department_name',)
    list_filter = ('department_name',)
    search_fields = ('department_name',)


admin.site.register(Departments, DepartmentsAdmin)
