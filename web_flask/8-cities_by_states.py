#!/usr/bin/python3

from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def remove(self):
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    states = storage.all("State")
    cities = storage.all("City")
    return render_template('8-cities_by_states.html',
                           states=states, cities=cities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
