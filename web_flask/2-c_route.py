#!/usr/bin/python3

from flask import Flask, escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return ("Hola HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    text = text.replace('_', ' ')
    return ('C {}'.format(text))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
