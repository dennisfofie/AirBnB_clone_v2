#!/usr/bin/python3
# creating web app for it to return variable in the route using default string

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    # print hello
    return 'Hello HBNB'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    # print hbnb
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    # print c is fun
    if '_' in text:
        text = text.replace('_', ' ')
    return f'C {text}'

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text='is cool'):
    # print python is cool
    if '_' in text:
        text = text.replace('_', ' ')
    return f'Python {text}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)