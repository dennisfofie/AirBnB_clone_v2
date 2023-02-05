#!/usr/bin/python3
# This script create route /hbnb to display HBNB

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    return 'Hello HBNB'

@app.route('/hbnb', strict_slashes=False)
def get_hbnb():
    return 'HBNB'


if __name__ == '__main__':
    app.run()