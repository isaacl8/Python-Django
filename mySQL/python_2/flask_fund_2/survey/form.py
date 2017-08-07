import random
from datetime import datetime
from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = 'redo_survey'

# This is the index page route
@app.route('/')
def index():
  return render_template('index.html')

# This route has the validation in it to verify the submited forms
@app.route('/process', methods=['POST'])
def process():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    # made it into an array to make it more condensed and easy to access will be called upon in the render_template
    form_data = [name, location, language, comment]
    # for loop is to cycle thru the validation with booleans in place.
    errors = False
    # key is refering to the name = "____" from the form in the index.html
    for key in request.form:
        if len(request.form[key]) == 0:
            flash(key + ' cannot be empty!')
            errors = True
        elif len(request.form[key]) > 120:
            flash(key + ' has to be less than 120!')
            errors = True
    # outside the for loop
    if errors == True:
        return redirect ('/')
    else:
        return render_template('result.html', form_data = form_data)

app.run(debug=True)
