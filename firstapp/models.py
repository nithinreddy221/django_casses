from django.db import models

# Create your models here.


class Departments(models.Model):
    id = models.IntegerField(primary_key=True,)
    department_name = models.CharField(max_length=100)
    dept_head = models.CharField(max_length=100)

    def __str__(self):
        return self.department_name