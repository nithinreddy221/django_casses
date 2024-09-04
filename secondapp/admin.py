from django.contrib import admin
from .models import Student, Teacher


# Register your models here.

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'address')
    list_filter = ('name', 'subject')
    search_fields = ('name', 'subject')


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'cls', 'teacher')
    list_filter = ('name',)
    search_fields = ('name',)


admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
