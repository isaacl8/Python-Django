from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    return render(request, 'first_app/index.html')

def results(request):
    return render(request, 'first_app/results.html')

def process(request):
    request.session['count'] += 1
    request.session ['name'] = request.POST['name']
    request.session ['loc'] = request.POST['location']
    request.session ['lang'] = request.POST['language']
    request.session ['comms'] = request.POST['comment']
    return redirect('/results')
