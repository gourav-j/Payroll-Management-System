from django.contrib import admin
from pms.models import UserProfileInfo, User, Job, Attendance
# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(Job)
admin.site.register(Attendance)