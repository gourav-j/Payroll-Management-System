# Generated by Django 2.0.13 on 2019-04-22 09:12

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('in', 'IN'), ('out', 'OUT')], default='in', max_length=3)),
                ('time', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_desc', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basic_salary', models.IntegerField()),
                ('dearness_allowance', models.IntegerField()),
                ('HRA', models.IntegerField()),
                ('conveyance_allowance', models.IntegerField()),
                ('entertainment_allowance', models.IntegerField()),
                ('percent_PF', models.IntegerField(default=12)),
                ('medical_insurance', models.IntegerField()),
                ('gross_salary', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfileInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dob', models.DateField()),
                ('gender', models.CharField(choices=[('m', 'Male'), ('f', 'Female')], default='m', max_length=1)),
                ('country', models.CharField(max_length=15)),
                ('state', models.CharField(max_length=15)),
                ('city', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=200)),
                ('pincode', models.CharField(max_length=6, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'Only 0-9 are allowed.'), django.core.validators.MinLengthValidator(6), django.core.validators.MaxLengthValidator(6)])),
                ('mobile_no', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'Only 0-9 are allowed.'), django.core.validators.MinLengthValidator(10), django.core.validators.MaxLengthValidator(10)])),
                ('job_desc', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pms.Job')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
