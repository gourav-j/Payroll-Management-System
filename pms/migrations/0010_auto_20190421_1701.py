# Generated by Django 2.0.13 on 2019-04-21 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pms', '0009_remove_attendance_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='status',
            field=models.CharField(choices=[('i', 'IN'), ('o', 'OUT'), ('n', 'VG')], default='i', max_length=1),
        ),
    ]