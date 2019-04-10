from django.test import TestCase
from django.contrib.auth.models import User

from .models import UserProfileInfo
# Create your tests here.

#Test Case for model
class UserTest(TestCase):
	def add_user(self):
		return User.objects.create_user(username="test1", first_name="test", last_name="test", email="test1@gmail.com", password="12345678")
	def register_user(self,user):
		return UserProfileInfo.objects.create(user=user, dob="2014-02-06", gender="m", country="India", state="Ktk", city="BLR", address="344 Ns Road", pincode=723456, mobile_no="4568796512")

	def test_creation(self):
		w=self.add_user()
		g=self.register_user(w)
		self.assertTrue(isinstance(g,UserProfileInfo))
