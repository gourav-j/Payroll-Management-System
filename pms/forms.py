from django import forms
from pms.models import UserProfileInfo
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password')

class DateInput(forms.DateInput):
	input_type = 'date'

class UserProfileInfoForm(forms.ModelForm):
     class Meta():
         model = UserProfileInfo
         fields = ('first_name','last_name','dob','gender','country','state','city','address','pincode','email_id','mobile_no')
         widgets = {
         	'dob': DateInput(),
         }