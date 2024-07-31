#!/usr/bin/python3
"""Starts a Flask web application to display states list"""


from models import storage
from flask import Flask, render_template
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """Close the storage on teardown"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Display a HTML page with a list of all State objects"""
    s = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=s)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
