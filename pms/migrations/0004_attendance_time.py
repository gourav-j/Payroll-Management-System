# Generated by Django 2.2 on 2019-04-22 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pms', '0003_auto_20190423_0327'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='time',
            field=models.TimeField(auto_now=True),
        ),
    ]