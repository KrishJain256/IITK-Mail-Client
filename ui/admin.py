from django.contrib import admin
from .models import *


class MailAdmin(admin.ModelAdmin):
    list_display = ['sender','reciever','subject','date_time']

class UserAdmin(admin.ModelAdmin):
    list_display = ['username','password']

admin.site.register(Mail)
admin.site.register(User)
