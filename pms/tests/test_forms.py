import datetime
from django.test import TestCase
from django.utils import timezone
from pms.forms import UserForm,AttendanceForm
# Create your tests here.

#Test Case for model
class FormTest(TestCase):
	def test_user_form_email_field_label(self):
		form = UserForm(data={'email': 'hellogmail.com'})
		self.assertFalse(form.is_valid())

	def test_attendance_form_status_field_label(self):
		form = AttendanceForm(data={'status': 'in'})
		self.assertTrue(form.is_valid())