#!/usr/bin/python3
""" script that starts a Flask web application
on port 5000 and displays Hello HBNB"""

from flask import Flask, escape, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def Hello():
    """ displaying a default Hello """
    return 'hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """ display HBNB """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def C(text):
    """ display C with the passed keyword argument var text """
    return 'C %s' % text.replace(text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """ display python with the passed keyword argument var text """
    return 'Python %s' % text.replace("_", " ")


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ display n is a number only if n is an integer """
    return '%d is a number' % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ Display a HTML page only if n is an integer """
    return render_template('5-number.html', n=n)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
