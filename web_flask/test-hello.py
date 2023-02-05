#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)

@app.route('/')
def return_hello():
    return 'This is something am texting'

if __name__ == '__main__':
    app.run()
