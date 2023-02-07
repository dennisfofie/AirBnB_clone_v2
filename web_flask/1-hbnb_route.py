#!/usr/bin/python3
"""
flask model
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """
    / home path
    """
    return 'Hello HBNB'

@app.route('/hbnb', strict_slashes=False)
def get_hbnb():
    """
    / hbnb path
    """
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)