from django.shortcuts import render, redirect
from .models import Course
# Create your views here.
def index(request):
    context = {
        "courses": Course.objects.all()
    }
    return render(request, 'course_app/index.html', context)

def process(request):
    Course.objects.create(name = request.POST['name'], description = request.POST['description'])
    return redirect('/')

def destroy(request,id):

    context = {
        "courses": Course.objects.filter(id=id)
    }
    return render(request, 'course_app/destroy.html', context, id )

def remove(request,id):
    course = Course.objects.get(id=id).delete()

    return redirect('/')
