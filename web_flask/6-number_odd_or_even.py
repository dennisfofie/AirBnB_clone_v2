#!/usr/bin/python3
# rendering html page on condition

from flask import Flask, render_template
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

@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text='is cool'):
    # print python is cool
    if '_' in text:
        text = text.replace('_', ' ')
    return f'Python {text}'

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    # print number
    return f'{n} is a number'

@app.route('/number_template/<int:n>', strict_slashes=False)
def if_n_is_int_template(n):
    # print n is number
    if type(n) is int:
        return render_template('5-number.html', number=n)

@app.route('/number_odd_or_even/<int:n>',strict_slashes=False)
def odd_even(n):
    # print odd or even
        return render_template('6-number_odd_or_even.html', number=n)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)