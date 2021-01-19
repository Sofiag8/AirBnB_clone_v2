#!/usr/bin/python3
""" script that starts a Flask web application
on port 5000 and displays Hello HBNB"""

from flask import Flask, escape

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
    """ display C with the passed keyword argument text """
    text = text.replace("_", " ")
    return 'C %s' % escape(text)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
