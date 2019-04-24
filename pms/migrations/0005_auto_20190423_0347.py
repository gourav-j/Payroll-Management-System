# Generated by Django 2.2 on 2019-04-22 22:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pms', '0004_attendance_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalaryStructure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basic_salary', models.IntegerField()),
                ('dearness_allowance', models.IntegerField()),
                ('HRA', models.IntegerField()),
                ('conveyance_allowance', models.IntegerField()),
                ('percent_PF', models.IntegerField(default=12)),
                ('medical_insurance', models.IntegerField()),
                ('gross_salary', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Salary',
        ),
    ]