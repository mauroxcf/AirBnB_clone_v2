#!/usr/bin/python3
""" display 2 message module """


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_holberton():
    """ function display hello hbnb"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def holberton():
    """ function display hello hbnb"""
    return "HBNB"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
