from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def index(request):
    if 'count' not in request.session:
        request.session['count'] = 1
    if 'random' not in request.session:
        request.session['random'] = get_random_string(14)
    return render(request, 'first_app/index.html')
def randomgen(request):
    request.session['count'] += 1
    request.session['random'] = get_random_string(14)
    return redirect('/')
