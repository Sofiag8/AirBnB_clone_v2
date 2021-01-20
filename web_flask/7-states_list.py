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


@app.route('/states_list', strict_slashes=False)
def display_states():
    """ display a HTML page nside the tag BODY, H1 tag for
    States, UL tag with the list of all State objects present
    in DBStorage sorted by name (A-Z). And LI tag for the
    description of one State:id:name. Check on
    file 7-states_list.html on templates"""
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
