#!/usr/bin/python3
# This application display c and the value of a variable in flask route

from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_HBNB():
    return 'Hello HBNB'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    if '_' in text:
        text = text.replace('_', ' ')
    return f'C {text}'

if __name__ == '__main__':
    app.run()