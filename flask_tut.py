
from crypt import methods
from django.http import request
from flask import Flask, redirect, url_for, render_template
from ex2fx import *


app = Flask(__name__)



@app.route('/')   #decorator. allows page to be displayed. catches all pages
def home(): 
    c = extract()
    d = transform(c)
    test = 'work in progress'        #
    return render_template('index0.html', value= test)

@app.route('/result', methods= ['POST', 'GET'])
def result():
    output = request()     #having an issue importing this from flask. only imports from django
    name = print(output['name'])

    return render_template('index0.html',name = 'name')

   
@app.route('/pizza/')   # redirect test page
def pizza():
    return render_template('quotes.html') 


if __name__ == "__main__":
    app.run(debug= True)