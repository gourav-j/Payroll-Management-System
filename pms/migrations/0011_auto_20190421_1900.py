# Generated by Django 2.0.13 on 2019-04-21 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pms', '0010_auto_20190421_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='status',
            field=models.CharField(choices=[('in', 'IN'), ('out', 'OUT')], default='i', max_length=3),
        ),
    ]