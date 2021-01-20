#!/usr/bin/python3
""" Script that starts a Flask web application
 listened on 0.0.0.0 port 5000 using storage and routing
 states_list
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def close(self):
    """ closing Session """
    storage.close()


@app.route('/states', strict_slashes=False)
def states():
    """ list states present in DBStorage sorted A-Z """
    states = storage.all(State)
    return render_template('9-states.html', states=states, mode="none")

@app.route('/states/<id>', strict_slashes=False)
def states_by_id(id):
    """ list the cities in a state found by its id """
    states = storage.all(State)
    for state in states.values():
        if state.id == id:
            return render_template('9-states.html', state=state, mode="id")
        else:
            return render_tmeplate('9-states.html', states=states, mode="not")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
