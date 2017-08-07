from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt

# Create your views here.
def index(request):
    return render(request, 'login_app/index.html')

def validate(request):
    if request.method == "POST":
        errors= User.objects.validate(request.POST)
        if errors:
            for error in errors:
                messages.error(request,error)
        else:
            messages.success(request, "The username you entered ({}) is valid. Thank you!".format(request.POST['username']))
            hashed_pass = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
            User.objects.create(username=request.POST['username'],password=hashed_pass)

            return redirect('/success')

    return redirect('/')

def success(request):
    context = {
        "users" : User.objects.all()
    }
    return render(request, 'login_app/success.html', context)

def login(request):
    if request.method == "POST":
        users = User.objects.filter(username=request.POST['username'])
        if users:
            user = users[0]
            hashed_pass = bcrypt.hashpw(request.POST['password'].encode(), user.password.encode())
            if user.password == hashed_pass:
                messages.success(request,"Successful login!")
                request.session['logged_user'] = user.id
                return redirect('/success')
                messages.error(request,"Invalid authentication credentials.")
    return redirect('/')
