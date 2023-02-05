#!/usr/bin/python3
# rendering html page if it is an integer

from flask import Flask, render_template
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

@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text='is cool'):
    if '_' in text:
        text = text.replace('_', ' ')
    return f'Python {text}'

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return f'{n} is a number'

@app.route('/number_template/<int:n>', strict_slashes=False)
def if_n_is_int_template(n):
    if type(n) is int:
        return render_template('5-number.html', number=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)