from django.shortcuts import render, redirect
import random
VALUES = ['populate this list with various strings', 'hello', 'im happy']
# Create your views here.
def index(request):
    return render(request, 'surprise_app/index.html')

def result(request):
    number = int(request.session['num'])
    context = {
    "words": VALUES[:number]
    }
    return render(request, 'surprise_app/results.html', context)

def process(request):
    request.session ['num'] = request.POST['num']
    return redirect('/results')
