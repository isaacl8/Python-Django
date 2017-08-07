from django.shortcuts import render, redirect
from .models import User


# Create your views here.

def index(request):
    return render(request,'wish_list_app/index.html')

def register(request):
    if request.method == "POST":
        form = request.POST
        User.objects.create(name=form['name'], username=form['username'], password=form['password'])
    return redirect("/dashboard")

def login(request):
    if request.method == "POST":
        form = request.POST
        user_check = User.objects.filter(username=form['username']).filter(password=form['password'])
    if user_check:
        user = user_check[0]
        request.session['user_id'] = user.id
        context = {
        "wish" : Wish.objects.all()
    }

    return redirect("/dashboard")

def dashboard(request):
    context = {
        "wish" : Wish.objects.all()
    }
    return render(request, 'wish_list_app/dashboard.html', context)

# def wish_item(request):
#    context = {
#        "wish" : Wish.objects.all(),
#         "user" : User.objects.all()
#    }
#    return render(request, 'wish_list_app/dashboard.html', context)

#
# def create(request):
#     if request.method == "POST":
#         form = request.POST
#     create = User.objects.create(item=form['item'])
#     if not item:
#         errors.append('item field is required')
#     if len(item) < 3:
#         errors.append('item must be at least 3 characters long')
#     return redirect ('/dashboard')
