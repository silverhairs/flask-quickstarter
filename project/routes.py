from project import app
from flask import render_template, url_for

@app.route('/')
def welcome():
    return render_template('welcome.html')