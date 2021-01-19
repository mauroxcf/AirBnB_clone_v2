#!/usr/bin/python3
""" display message module """


from flask import Flask, render_template
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
    """ function display a text or a default value"""
    text = text.replace('_', ' ')
    return "Python %s" % text


@app.route('/number/<int:n>', strict_slashes=False)
def display_integer(n):
    """ function display a number"""
    return "%d is a number" % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_html(n):
    """ function display a html only if n in a integer"""
    return render_template('5-number.html', num=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
