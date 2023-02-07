#!/usr/bin/python3
# passing number as a variable to the number route

from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_HBNB():
    #hello
    return 'Hello HBNB'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    #print hbnb
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    # print  c is fun
    if '_' in text:
        text = text.replace('_', ' ')
    return f'C {text}'

@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text='is cool'):
    # print python is cool
    if '_' in text:
        text = text.replace('_', ' ')
    return f'Python {text}'

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    # print n
    return f'{n} is a number'