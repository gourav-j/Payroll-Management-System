# Generated by Django 2.2 on 2019-04-22 22:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pms', '0008_remove_salarystructure_gross_salary'),
    ]

    operations = [
        migrations.RenameField(
            model_name='salarystructure',
            old_name='dearness_allowance',
            new_name='DA',
        ),
    ]
