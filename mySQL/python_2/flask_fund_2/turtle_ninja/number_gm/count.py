from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'redo'


@app.route('/')
def index():
  return render_template("index.html")
# 
# @app.route('/process')












app.run(debug=True)
