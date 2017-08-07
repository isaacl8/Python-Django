from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'first_app/index.html')

def ninjas(request):
    return render(request, 'first_app/ninjas.html')


def colors(request, color):
    if color == 'purple':
        color = '/static/first_app/images/donatello.jpg'
    elif color == 'red':
        color = '/static/first_app/images/raphael.jpg'
    elif color == 'blue':
        color = '/static/first_app/images/leonardo.jpg'
    elif color == 'orange':
        color = '/static/first_app/images/michelangelo.jpg'
    else:
        color = '/static/first_app/images/notapril.jpg'

    context ={
        'color': color
    }
    return render(request, 'first_app/colors.html', context)
