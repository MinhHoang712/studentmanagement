from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, AdminHod, Staffs, Courses, Subjects, Students,Attendance, AttendanceReport, LeaveReportStaff, LeaveReportStudent, FeedBackStaffs, FeedBackStudent, NotificationStaffs, NotificationStudent

# Register your models here.
class UserModel(UserAdmin):
    pass  
admin.site.register(CustomUser, UserModel)
admin.site.register(AdminHod)
admin.site.register(Staffs)
admin.site.register(Courses)
admin.site.register(Subjects)
admin.site.register(Students)
admin.site.register(Attendance)
admin.site.register(AttendanceReport)
admin.site.register(LeaveReportStudent)
admin.site.register(LeaveReportStaff)
admin.site.register(FeedBackStudent)
admin.site.register(FeedBackStaffs)
admin.site.register(NotificationStudent)
admin.site.register(NotificationStaffs)