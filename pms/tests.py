from django.test import TestCase

from .models import UserProfileInfo
# Create your tests here.

#Test Case for model
class UserTest(TestCase):
	def create_user(self, username="test1", password="12345678", first_name="test", last_name="test", dob="2014-02-06", gender="m", country="India", state="Ktk", city="BLR", address="344 Ns Road", pincode=723456, email_id="test1@gmail.com", mobile_no="4568796512"):
		return UserProfileInfo.objects.create(username=username,password=password,first_name=first_name,last_name=last_name,dob=dob,gender=gender,country=country,state=state,city=city,address=address,pincode=pincode,email_id=email_id,mobile_no=mobile_no)

	def test_creation(self):
		w=self.create_user()
		self.assertTrue(isinstance(w,UserProfileInfo))
