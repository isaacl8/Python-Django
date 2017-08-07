from flask import Flask, render_template, redirect, request
app = Flask(__name__)

# this will be the home page function.
@app.route('/')
def index():
    return render_template('index.html')

# This will have the function will have diff ninjas.
@app.route('/ninja/<color>')
def ninja(color):
    if color == 'ninja':
        src = 'img/tmnt.png'
    elif color == 'purple':
        src = 'img/donatello.jpg'
    elif color == 'red':
        src = 'img/raphael.jpg'
    elif color == 'blue':
        src = 'img/leonardo.jpg'
    elif color == 'orange':
        src = 'img/michelangelo.jpg'
    else:
        src = 'img/notapril.jpg'
    return render_template('color.html', src = src)












app.run(debug=True)
