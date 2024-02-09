#!/usr/bin/python3
<<<<<<< HEAD
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /cities_by_states: HTML page with a list of all states and related cities.
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
@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """Displays an HTML page with a list of all states and related cities.

    States/cities are sorted by name.
    """
    states = storage.all("State")
=======
@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states_route():
    """
    Cities by states: display a HTML page: (inside the tag BODY)
    Returns:
        html: template that lists all states sort by name A->Z
    """
    states = storage.all("State").values()
>>>>>>> fbc8b3ff7d981ae766ee7c2a86ad1ace0f06995f
    return render_template("8-cities_by_states.html", states=states)


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
