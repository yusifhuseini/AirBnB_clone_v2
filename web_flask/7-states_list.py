#!/usr/bin/python3
<<<<<<< HEAD
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /states_list: HTML page with a list of all State objects in DBStorage.
"""
from models import storage
from flask import Flask
=======
"""
A script that starts a Flask web application:
"""

from flask import Flask
from models import storage
>>>>>>> fbc8b3ff7d981ae766ee7c2a86ad1ace0f06995f
from flask import render_template

app = Flask(__name__)


<<<<<<< HEAD
@app.route("/states_list", strict_slashes=False)
def states_list():
    """Displays an HTML page with a list of all State objects in DBStorage.

    States are sorted by name.
    """
    states = storage.all("State")
=======
@app.route('/states_list', strict_slashes=False)
def states_list_route():
    """
    List states: display a HTML page: (inside the tag BODY)
    Returns:
        html: template that lists all states sort by name A->Z
    """
    states = storage.all("State").values()
>>>>>>> fbc8b3ff7d981ae766ee7c2a86ad1ace0f06995f
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
<<<<<<< HEAD
def teardown(exc):
    """Remove the current SQLAlchemy session."""
=======
def close_db(exception=None):
    """
    After each request remove the current SQLAlchemy Session:
    """
>>>>>>> fbc8b3ff7d981ae766ee7c2a86ad1ace0f06995f
    storage.close()


if __name__ == "__main__":
<<<<<<< HEAD
    app.run(host="0.0.0.0")
=======
    app.run(host="0.0.0.0", port=5000)
>>>>>>> fbc8b3ff7d981ae766ee7c2a86ad1ace0f06995f
