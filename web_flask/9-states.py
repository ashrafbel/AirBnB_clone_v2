#!/usr/bin/python3
"""Starts a Flask for display a list of states"""


from models import storage
from flask import Flask, render_template
from models.state import State

app = Flask(__name__)

@app.teardown_appcontext
def teardown_db(exception):
    """Close the storage"""
    storage.close()

@app.route('/states_list', strict_slashes=False)
def states_list():
    """list of all State objects in pages html"""
    s = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=s)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

