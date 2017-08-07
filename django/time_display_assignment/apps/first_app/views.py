from django.shortcuts import render
import datetime
# import time

# Create your views here.
def index(request):
    mydate = datetime.datetime.now()
    context = {
    'date': mydate
    }
    return render(request,'first_app/index.html', context)
