import random
from datetime import datetime
from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = 'redo_ninja'

# Home page, which also has session checking the coin count
@app.route('/')
def index():
    if 'my_coins' not in session:
        session['my_coins'] = 0
        # print session['coin']
    if 'activity_log' not in session:
        session['activity_log'] = []
    return render_template('index.html')

# processes the submit forms and calculates the money
@app.route('/process_money', methods=['POST'])
def process():

    # The farm form will be adding a random number between 10-20
    if request.form['action'] == 'farm':
        farm_add = random.randrange(10, 21)
        session['my_coins'] += farm_add
        log = 'You have earned ' + \
            str(farm_add) + ' gold coins.' + str(datetime.now().strftime("%Y/%m/%d %I:%M%p"))
        session['activity_log'].append(log)

    # The cave form will be adding a random number between 5-10
    elif request.form['action'] == 'cave':
        farm_add = random.randrange(5, 11)
        session['my_coins'] += farm_add
        log = 'You have earned ' + str(farm_add) + ' gold coins.' + \
            str(datetime.now().strftime("%Y/%m/%d %I:%M%p"))
        session['activity_log'].append(log)

    # The house form will be adding a random number between 2-5
    elif request.form['action'] == 'house':
        farm_add = random.randrange(2, 6)
        session['my_coins'] += farm_add
        log = 'You have earned ' + str(farm_add) + ' gold coins.' + \
            str(datetime.now().strftime("%Y/%m/%d %I:%M%p"))
        session['activity_log'].append(log)
    # The casino form will be adding or subtracting a random number between 0-50
    elif request.form['action'] == 'casino':
        # the chance variable os allowing it to be random for the chance of earning or losing gold.
        # if chance == 0 gold will be added if not, it will result to losing gold.
        chance = random.randrange(0, 2)
        if chance == 0:
            farm_add = random.randrange(-50, 51)
            session['my_coins'] += farm_add
            log = 'You have earned ' + str(farm_add) + ' gold coins.' + \
                str(datetime.now().strftime("%Y/%m/%d %I:%M%p"))
            session['activity_log'].append(log)
        elif chance == 1:
            farm_add = random.randrange(-50, 51)
            session['my_coins'] -= farm_add
            log = 'You have lost ' + str(farm_add) + ' gold coins.' + \
                str(datetime.now().strftime("%Y/%m/%d %I:%M%p"))
            session['activity_log'].append(log)
    # the process function redirects to the home page.
    return redirect('/')


app.run(debug=True)
