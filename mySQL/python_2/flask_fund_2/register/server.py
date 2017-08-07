from flask import Flask, render_template, redirect, request, session, flash
# W/regex
import re

app = Flask(__name__)
app.secret_key = 'resgistration_redo'
# valiodation
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]')
PW_REGEX = re.compile(r'^.{8,}$')

@app.route('/')
def index():
    return render_template('index.html')
# Using flash with categories
@app.route('/process', methods=['POST'])
def process():
    # using the boolean with the function, one inside the for loop and one outside it
    errors = False
    # key is refering to the name = "____" from the form in the index.html
    for key in request.form:
        if len(request.form[key]) == 0:
            flash(key + ' cannot be empty!')
            errors = True
    # outside the for loop
    if errors == True:
        pass
    # using regex for valiodation of POST in form
    elif not EMAIL_REGEX.match(request.form['Email']):
        flash('Email Not valid', 'error')
    elif not PW_REGEX.match(request.form['Password']):
        flash('password must be min 8 characters', 'error')
    elif request.form['Password'] != request.form['Confirm Password']:
        flash('passwords must match', 'error')
    else:
        flash('Thanks for submitting your information.', 'success')
    return redirect('/')

app.run(debug=True)
