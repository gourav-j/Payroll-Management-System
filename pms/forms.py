from django import forms
from pms.models import UserProfileInfo,Attendance
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
import datetime

class DateInput(forms.DateInput):
    input_type = 'date'


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','first_name','last_name','email','password')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control','placeholder':'Username'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control','placeholder':'Email'}),
            'password': forms.TextInput(attrs={'class': 'form-control','placeholder':'Password'}),
            'confirm_password': forms.TextInput(attrs={'class': 'form-control','placeholder':'Confirm Password'}),
        }
    '''def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not first_name:
            raise forms.ValidationError("This field is mandatory")'''
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if not email:
            raise forms.ValidationError("This field is mandatory")
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError('Email address already exists.')
        return email

    def clean_confirm_password(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("password and confirm_password do not match")


class UserProfileInfoForm(forms.ModelForm):
     class Meta():
         model = UserProfileInfo
         fields = ('dob','gender', 'job_desc', 'street', 'city', 'state', 'country', 'pincode', 'mobile_no')
         widgets = {
         	'dob': DateInput(attrs={'class':'input-group'}),
            'street': forms.TextInput(attrs={'class': 'form-control','placeholder':'Street'}),
            'city': forms.TextInput(attrs={'class': 'form-control','placeholder':'City'}),
            'state': forms.TextInput(attrs={'class': 'form-control','placeholder':'State'}),
            'country': forms.TextInput(attrs={'class': 'form-control','placeholder':'Country'}),
            'pincode': forms.TextInput(attrs={'class': 'form-control','placeholder':'Pincode'}),
            'mobile_no': forms.TextInput(attrs={'class': 'form-control','placeholder':'Mobile no'}),
         }

class EditUserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'email')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control','placeholder':'Email'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if not email:
            raise forms.ValidationError("This field is mandatory")
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError('Email address already exists.')
        return email

class EditUserProfileInfoForm(forms.ModelForm):
    class Meta():
         model = UserProfileInfo
         fields = ('dob','gender', 'job_desc', 'country','state','city','street','pincode','mobile_no')
         widgets = {
            'dob': DateInput(attrs={'class':'input-group'}),
            'street': forms.TextInput(attrs={'class': 'form-control','placeholder':'Street'}),
            'city': forms.TextInput(attrs={'class': 'form-control','placeholder':'City'}),
            'state': forms.TextInput(attrs={'class': 'form-control','placeholder':'State'}),
            'country': forms.TextInput(attrs={'class': 'form-control','placeholder':'Country'}),
            'pincode': forms.TextInput(attrs={'class': 'form-control','placeholder':'Pincode'}),
            'mobile_no': forms.TextInput(attrs={'class': 'form-control','placeholder':'Mobile no'}),
         }

class AttendanceForm(forms.ModelForm):
    class Meta():
        model = Attendance
        fields = ('status',)
