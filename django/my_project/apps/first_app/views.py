from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    context = {
        'greeting': "hello",
        'place':"world"
    }
    return render(request,'first_app/index.html', context)

def register(request):
    print request.POST['username'], request.POST['password']

    request.session['username'] = request.POST['username']
    request.session['password'] = request.POST['password']
    return redirect('/')
