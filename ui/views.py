from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Mail
from .forms import *
from .mysql_helper import user_functions
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse
import simplejson

username = ""
password = ""

def userclient(request):
    uploadjson(1)
    global username
    emails = Mail.objects.filter(receiver=username)
    emails1 = Mail.objects.filter(receiver=username).values('sender','receiver','subject','body','date_time')
    emails2 = Mail.objects.values()
    print(JsonResponse(list(emails2),safe=False))
    emails_json = json.dumps(list(emails2),cls=DjangoJSONEncoder)
    save_file = open("messages.json", "w")
    json.dump(emails_json, save_file, indent=6)
    save_file.close()
    return render(request, 'userclient.html',{'emails_json':emails_json,'emails':emails})

def login(request):
    global username
    global password
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = loginform(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            verify = user_functions.verify_user(username, password)
            if verify == 1:
                # redirect to a new URL:
                return HttpResponseRedirect("/ui/userclient/")
            else:
                return HttpResponseRedirect("/ui/login/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = loginform()

    return render(request, "login.html", {"form": form})

def signup(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = signupform(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            data = form.cleaned_data
            firstname = data['firstname']
            lastname = data['lastname']
            rollno = data['rollno']
            username = data['username']
            email = data['email']
            password = data['password']

            user_functions.create_new_user(username,password,firstname,lastname,email,rollno)

            # redirect to a new URL:
            return HttpResponseRedirect("/ui/login/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = signupform()

    return render(request, "signup.html", {"form": form})


def uploadjson(request):
    global username
    emails2 = Mail.objects.filter(receiver=username).values()
    emails_json = json.dumps(list(emails2), cls=DjangoJSONEncoder)
    save_file = open("messages.json", "w")
    json.dump(emails_json, save_file, indent=6)
    save_file.close()
    return HttpResponse(emails_json)

def compose(request):
    global username
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = signupform(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            data = form.cleaned_data
            to = data['to']
            subject = data['subject']
            body = data['body']

            user_functions.send_mail(username,to,subject,body)

            # redirect to a new URL:
            return HttpResponseRedirect("/ui/userclient/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = composeform()

    return render(request, "compose.html", {"form": form})



