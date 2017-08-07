from django.shortcuts import render

# Create your views here.
def index(request):
    # displays index.html
    return render(request, 'first_app/index.html')

def projects(request):
    # displays projects.html
    return render(request, 'first_app/projects.html')

def about(request):
    # displays about.html
    return render(request, 'first_app/about.html')

def testimonials(request):
    # displays test.html
    return render(request,'first_app/test.html')
