from django.test import TestCase
from django.contrib.auth.models import User

from .models import UserProfileInfo, Job
# Create your tests here.

#Test Case for model
class Test1(TestCase):
	def setUp(self):
		Job.objects.create(job_desc='SDE1')
		User.objects.create_user(username="test10", first_name="test", last_name="test", email="test1@gmail.com", password="12345678")
		user=User.objects.get(username='test10')
		job=Job.objects.get(job_desc='SDE1')
		UserProfileInfo.objects.create(user=user, dob="2014-02-06", gender="m", job_desc=job, country="India", state="Ktk", city="BLR", street="344 Ns Road", pincode=723456, mobile_no="4568796512")

	def test1(self):
		job=Job.objects.get(job_desc='SDE1')
		self.assertTrue(isinstance(job,Job))
		us=User.objects.get(username='test10')
		g=UserProfileInfo.objects.get(user=us)
		self.assertTrue(isinstance(g,UserProfileInfo))


'''
from django.test import TestCase
from django.contrib.auth.models import User

from .models import UserProfileInfo, Job
# Create your tests here.

#Test Case for model
class Test1(TestCase):
	def add_job(self):
		return Job.objects.create(job_desc='SDE1')
	def add_user(self):
		return User.objects.create_user(username="test10", first_name="test", last_name="test", email="test1@gmail.com", password="12345678")
	def register_user(self, user, job):
		return UserProfileInfo.objects.create(user=user, dob="2014-02-06", gender="m", job_desc=job, country="India", state="Ktk", city="BLR", address="344 Ns Road", pincode=723456, mobile_no="4568796512")

	def test_creation(self):
		job=self.add_job()
		self.assertTrue(isinstance(job,Job))
		w=self.add_user()
		g=self.register_user(w,job)
		self.assertTrue(isinstance(g,UserProfileInfo))
'''