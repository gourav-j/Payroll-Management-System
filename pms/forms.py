from django import forms
from pms.models import UserProfileInfo
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','first_name','last_name','email','password')

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not first_name:
            raise forms.ValidationError("This field is mandatory")
        
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

class DateInput(forms.DateInput):
	input_type = 'date'

class UserProfileInfoForm(forms.ModelForm):
     class Meta():
         model = UserProfileInfo
         fields = ('dob','gender','country','state','city','address','pincode','mobile_no')
         widgets = {
         	'dob': DateInput(),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
         }
