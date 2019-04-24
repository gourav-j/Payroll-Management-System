from django.contrib import admin
from pms.models import UserProfileInfo, User, Job, Attendance, SalaryStructure, Salary
# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(Job)
admin.site.register(Attendance)
admin.site.register(SalaryStructure)
admin.site.register(Salary)