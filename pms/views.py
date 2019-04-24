from django.shortcuts import render, redirect
from pms.forms import UserForm,UserProfileInfoForm,EditUserForm,EditUserProfileInfoForm,AttendanceForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from payroll import settings
from django import forms
from pms.models import User,Attendance, SalaryStructure, UserProfileInfo, Salary
from django.utils import timezone
from datetime import date
from .render import Render


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
        return render(request,'pms/login.html',{'registered':registered})
    return render(request,'pms/signup.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})

def user_login(request):
    if request.session.has_key('username'):
        username = request.session['username']
        return render(request,'pms/index.html')
    loginFail = False
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request,user)
            request.session['username'] = username
            if user.is_superuser:
                return HttpResponseRedirect(reverse('admin:index'))
            else:
                return HttpResponseRedirect(reverse('index'))
        else:
            loginFail = True
            return render(request, 'pms/login.html', {'loginFail':loginFail})
    else:
        return render(request, 'pms/login.html', {'loginFail':loginFail})

@login_required
def user_edit(request):
    if not request.session.has_key('username'):
        return render(request,'pms/index.html')

    user_form = EditUserForm(data = request.POST or None, instance = request.user)
    u_p = request.user.userprofileinfo
    profile_form = EditUserProfileInfoForm(data = request.POST or None, instance = u_p)
    
    if request.method == 'POST':
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect(reverse('index'))
        else:
            return render(request, 'pms/edit_profile.html',{'user_form':user_form, 'profile_form':profile_form})
        
    else:
        return render(request, 'pms/edit_profile.html',{'user_form':user_form, 'profile_form':profile_form})

@login_required
def view_profile(request):
    args = {'user':request.user, 'userprofileinfo':request.user.userprofileinfo}
    return render(request, 'pms/view_profile.html', args)

@login_required
def attendance(request):
    if not request.session.has_key('username'):
        return render(request,'pms/index.html')
    done = 0
    status=''
    attendance = Attendance.objects.filter(user = request.user, date = date.today())
    cnt = attendance.count()
    if request.method == 'POST':
        attendance_form = AttendanceForm(data = request.POST)
        if attendance_form.is_valid():
            if cnt==1:
                for a in attendance:
                    if a.status==request.POST.get('status'):
                        status=a.status
                        return render(request,'pms/attendance.html',{'status':status,'done':done})
            
            temp = attendance_form.save(commit=False)
            user = User.objects.get(username=request.user.username)
            temp.user = user
            temp.save()
            return redirect(reverse('index'))
        else:
            return render(request, 'pms/attendance.html',{'attendance_form':attendance_form})
    else:
        attendance_form = AttendanceForm()
        if cnt==2:
            done = 3
        return render(request, 'pms/attendance.html',{'attendance_form':attendance_form,'done':done})

@login_required
def gen_attendance_pdf(request):
    if request.method=='POST':
        first_date = request.POST.get('fromdate')
        last_date = request.POST.get('todate')
        attendance = Attendance.objects.filter(user = request.user, date__range=(first_date,last_date))
        today = timezone.now()
        params={
            'attendance':attendance,
            'user':request.user,
            'today':today
        }
        return Render.render('pms/attendance_report.html',params)
    else:
        return render(request,'pms/attendance_date_pick.html')

@login_required
def show_salary(request):
    user = request.user
    structure = SalaryStructure.objects.get(user=user)
    userprofileinfo = UserProfileInfo.objects.get(user=user)
    position = userprofileinfo.job_desc
    pf = structure.basic_salary+structure.DA+structure.HRA
    pf = pf*0.12
    gross = structure.basic_salary+structure.DA+structure.HRA+structure.conveyance_allowance+structure.bonus-pf-structure.medical_insurance
    args = {'structure':structure,'today':timezone.now(),'pf':pf,'gross':gross,'position':position}
    return render(request, 'pms/show_salary.html', args)

@login_required
def gen_salary_pdf(request):
    if request.method=='POST':
        first_date = request.POST.get('fromdate')
        last_date = request.POST.get('todate')
        salary = Salary.objects.filter(user = request.user, date__range=(first_date,last_date))
        structure = SalaryStructure.objects.get(user = request.user)
        pf = structure.basic_salary+structure.DA+structure.HRA
        pf = pf*0.12
        today = timezone.now()
        params={
            'salary':salary,
            'salstr':structure,
            'pf':pf,
            'user':request.user,
            'today':today
        }
        return Render.render('pms/salary_report.html',params)
    else:
        return render(request,'pms/salary_date_pick.html')