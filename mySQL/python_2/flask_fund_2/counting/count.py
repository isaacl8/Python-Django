from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'redo'

# Home page
@app.route('/')
def index():
    if session.get('number') is None and session.get('text') is None:
        session['number'] = random.randint(0, 100)
        session['text'] = ''
    return render_template('index.html', text=session['text'])

# processes the guess from the submitted form
@app.route('/process', methods=['POST'])
def process():

    number = int(request.form['num'])

    if number < session['number']:
        session['text'] = "Your number is too low!"
    elif number > session['number']:
        session['text'] = "Your number is too high!"
    elif number == session['number']:
        session['text'] = "Your number is perfect!"

    return redirect('/')

# reset game route
@app.route('/reset', methods=['POST'])
def reset():

    session.pop('text')
    session.pop('number')

    return redirect('/')

app.run(debug=True)
