# Generated by Django 2.2 on 2019-04-22 22:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pms', '0005_auto_20190423_0347'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salarystructure',
            name='gross_salary',
        ),
    ]
