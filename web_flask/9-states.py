#!/usr/bin/python3

from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def remove(self):
    storage.close()


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    if id is not None:
        id = "State." + id
    print(id)
    states = storage.all("State")
    cities = storage.all("City")
    return render_template('9-states.html',
                           states=states, cities=cities, id=id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
