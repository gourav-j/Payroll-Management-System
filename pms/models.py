from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator, RegexValidator
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class UserProfileInfo(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	dob = models.DateField()
	GENDER = (
		('m', 'Male'),
		('f', 'Female'),
	)
	gender = models.CharField(
		max_length=1,
        choices=GENDER,
        default='m',
	)
	job_desc = models.ForeignKey('Job', on_delete=models.SET_NULL, null=True)
	country = models.CharField(max_length = 15)
	state = models.CharField(max_length = 15)
	city = models.CharField(max_length = 15)
	street = models.CharField(max_length = 200)
	pincode = models.CharField(max_length=6,
		validators=[
			 RegexValidator(
                r'^[0-9]*$',
                'Only 0-9 are allowed.',
            ),
            MinLengthValidator(6),
            MaxLengthValidator(6),
		],)
	mobile_no = models.CharField(max_length=10,
		validators=[
			 RegexValidator(
                r'^[0-9]*$',
                'Only 0-9 are allowed.',
            ),
            MinLengthValidator(10),
            MaxLengthValidator(10),
		],)
	def __str__(self):
		return self.user.first_name

#	job_id = models.ForeignKey('Job', on_delete=models.CASCADE)
class Job(models.Model):
	job_desc = models.CharField(max_length=200, null=True)
	def __str__(self):
		return self.job_desc

class Attendance(models.Model):
	user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
	STATUS = (
		('in', 'IN'),
		('out', 'OUT'),
	)
	status = models.CharField(max_length=3, choices = STATUS, default='in')
	date = models.DateField(auto_now=True)
	time = models.TimeField(auto_now=True)
	def __str__(self):
		return f'{self.user.username},{self.time},{self.status}'

class SalaryStructure(models.Model):

	user = models.ForeignKey(User,on_delete=models.CASCADE)
	basic_salary = models.IntegerField()
	DA = models.IntegerField()
	HRA = models.IntegerField()
	conveyance_allowance = models.IntegerField()
	bonus = models.IntegerField(default=0)
	percent_PF = models.IntegerField(default = 12)  #on basic+da+hra
	medical_insurance = models.IntegerField()
	
	def __str__(self):
		return f'{self.user.username}: {self.basic_salary}'

class Salary(models.Model):
	user = models.ForeignKey(User,on_delete = models.CASCADE)
	gross_salary = models.IntegerField()
	leave = models.IntegerField(default=0)
	date = models.DateField(auto_now = True)

	def __str__(self):
		return f'[{self.date}]{self.user.username}: {self.gross_salary}'