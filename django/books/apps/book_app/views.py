from django.shortcuts import render, redirect
from .models import Book
# Create your views here.
def index(request):
    context = {
        "books": Book.objects.all()
    }
    return render(request, 'book_app/index.html', context)

def process(request):
    Book.objects.create(title=request.POST['titles'], category=request.POST['category'], author=request.POST['author'])
    return redirect('/')
