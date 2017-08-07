from django.shortcuts import render, redirect
from .models import User


# Create your views here.

def index(request):
    return render(request,'login_app/index.html')

def register(request):
    if request.method == "POST":
        form = request.POST
        #Validated Registration here
        User.objects.create(first_name=form['first_name'], last_name=form['last_name'], email=form['email'], password=form['password'])
    return redirect("logins:index")

def login(request):
    if request.method == "POST":
        form = request.POST
        user_check = User.objects.filter(email=form['email'])
    if user_check:
        user = user_check[0]
        request.session['user_id'] = user.id

    return redirect("secrets:dashboard")
