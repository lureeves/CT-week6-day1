from app import app
from flask import render_template

@app.route('/')
def index():
    return "Try /fave_5 instead"

@app.route('/fave_5')
def fave_list():
    return render_template('index.html')