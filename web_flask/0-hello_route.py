#!/usr/bin/python3
# creating a route to listen at localhost port 5000 and it should output hello

from flask import Flask
app = Flask(__name__)

app.route('/', strict_slashes=False)
def get_hello():
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run()
