from django.contrib import admin

# Register your models here.
from app import  models
admin.site.register(models.meeting)
admin.site.register(models.staff)
admin.site.register(models.department)
admin.site.register(models.meetingroom)
admin.site.register(models.UserInfor)
admin.site.register(models.sudo)
