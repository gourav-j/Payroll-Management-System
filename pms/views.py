from django.shortcuts import render, redirect
from pms.forms import UserForm,UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from payroll import settings
#from django.conf import settings

def index(request):
    return render(request,'pms/index.html')

@login_required
def user_logout(request):
    logout(request)
    try:
        del request.session['username']
    except:
        pass
    return HttpResponseRedirect(reverse('index'))


def signup(request):
    registered = False
    if request.session.has_key('username'):
        username = request.session['username']
        return render(request,'pms/index.html')
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            subject = 'Thank you for registering to our site'
            message = ' It  means a world to us '
            email_from = settings.EMAIL_HOST_USER
            print(email_from)
            recipient_list = [request.POST.get('email'),]
            send_mail( subject, message, email_from, recipient_list )
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
        return render(request,'pms/signup.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})

    if registered:
        return render(request,'pms/login.html')
    return render(request,'pms/signup.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})

def user_login(request):
    if request.session.has_key('username'):
        username = request.session['username']
        return render(request,'pms/index.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                request.session['username'] = username
                if user.is_superuser:
                    return HttpResponseRedirect(reverse('admin:index'))
                else:
                    return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            return HttpResponse("Invalid login details given.")
    else:
        return render(request, 'pms/login.html', {})
