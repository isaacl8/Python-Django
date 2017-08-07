from django. shortcuts import render, redirect
import random


def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activities' not in request.session:
        request.session['activities'] = ''
    return render(request,'first_app/index.html')

def process(request):
    choice = request.POST['choice']
    if choice == 'farm':
        gold = random.randrange(10,20)
    elif choice == 'cave':
        gold = random.randrange(5,10)
    elif choice == 'house':
        gold = random.randrange(2,5)
    else:
        gold = random.randrange(-50,51)

    if (gold > 0):
        text = 'Earned ' + str(gold) + 'golds from the ' + choice + '!'
    elif (gold < 0):
        text = 'Ouch! You entered a ' + choice + ' and lost ' + str(gold) + ' golds!'

    request.session['gold'] += gold
    request.session['activities'] += text + '\n'

    return redirect('/')
