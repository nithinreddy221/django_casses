# Generated by Django 3.2.25 on 2024-09-06 01:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='start_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 9, 6, 7, 23, 6, 895592)),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='start_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 9, 6, 7, 23, 6, 895592)),
        ),
    ]
