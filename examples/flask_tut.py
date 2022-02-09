from aem import app
from flask import Flask, redirect, url_for, render_template
from ex2fx import *


app = Flask(__name__)

c = extract()
d =  transform(c)

@app.route('/')   #decorator. allows page to be displayed. catches all pages
def home():         #
    return render_template('index.0.html', d = d)

@app.route('/result/')
def result():
    return render_template


@app.route('/pizza/')   # redirect test page
def pizza():
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run()