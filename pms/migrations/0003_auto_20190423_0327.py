# Generated by Django 2.2 on 2019-04-22 21:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pms', '0002_auto_20190422_1449'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendance',
            old_name='time',
            new_name='date',
        ),
    ]
