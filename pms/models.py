from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
# Create your models here.
class UserProfileInfo(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	dob = models.DateField(help_text='YYYY-MM-DD')
	GENDER = (
		('m', 'Male'),
		('f', 'Female'),
	)
	gender = models.CharField(
		max_length=1,
        choices=GENDER,
        default='m',
	)
	country = models.CharField(max_length = 15)
	state = models.CharField(max_length = 15)
	city = models.CharField(max_length = 15)
	address = models.CharField(max_length = 200)
	pincode = models.IntegerField(validators=[MinValueValidator(100000),MaxValueValidator(999999)])
	email_id = models.EmailField(primary_key=True)
	mobile_no = models.CharField(max_length=10)
	def __str__(self):
		return self.user.username
#	job_id = models.ForeignKey('Job', on_delete=models.CASCADE)
'''class Job(models.Model):
	job_id = models.CharField(max_length=15)
	job_title = models.CharField(max_length=50)
	job_desc = models.CharField(max_length=200, null=True)
'''
