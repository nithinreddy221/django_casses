from django.db import models
from datetime import datetime


class BaseSchoolModel(models.Model):
    start_date = models.DateTimeField(default=datetime.now(), blank=True)
    end_date = models.DateTimeField()
    address = models.TextField()

    class Meta:
        abstract = True


class Teacher(BaseSchoolModel):
    name = models.CharField(max_length=100, blank=False, null=False)
    subject = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Student(BaseSchoolModel):
    name = models.CharField(max_length=100, blank=False, null=False)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='students')
    cls = models.CharField(max_length=20)

    def __str__(self):
        return self.name
