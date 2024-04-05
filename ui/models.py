from django.db import models
import datetime

class Mail(models.Model):
    sender = models.CharField(max_length=255,default="<no-sender>")
    receiver = models.CharField(max_length=255,default="<no-receiver>")
    subject = models.CharField(max_length=255,default="<no-subject>")
    body = models.TextField(max_length=255)
    date_time = models.DateTimeField(default=datetime.datetime.now)

class User(models.Model):
    username = models.CharField(max_length=255,default="<no-user>")
    password = models.CharField(max_length=255,default="<no-passwd>")
    firstname = models.CharField(max_length=100,default="no-name>")
    lastname = models.CharField(max_length=100,default="<no-name>")
    email = models.EmailField(max_length=254,default="<no-email>")
    rollno = models.IntegerField(default=000000)
