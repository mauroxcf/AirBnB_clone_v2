#!/usr/bin/python3
""" display message module """


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_holberton():
    """ function display hello hbnb"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def holberton():
    """ function display hbnb"""
    return "HBNB!"


@app.route('/c/<text>', strict_slashes=False)
def c_is(text):
    """ function display a text"""
    text = text.replace('_', ' ')
    return "C %s" % text


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is(text):
    """ function display a text"""
    text = text.replace('_', ' ')
    return "Python %s" % text


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
