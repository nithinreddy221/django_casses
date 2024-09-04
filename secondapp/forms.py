from django import forms
from .models import Teacher, Student


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name', 'subject', 'start_date', 'end_date', 'address']


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'teacher', 'cls', 'start_date', 'end_date', 'address']
