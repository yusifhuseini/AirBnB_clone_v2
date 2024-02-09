#!/usr/bin/python3
<<<<<<< HEAD
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /hbnb: HBnB home page.
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
@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays the main HBnB filters HTML page."""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    places = storage.all("Place")
    return render_template("100-hbnb.html",
                           states=states, amenities=amenities, places=places)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
=======
@app.route('/hbnb', strict_slashes=False)
def states_list_route():
    """
    List all cities a of states: display a HTML page: (inside the tag BODY)
    Returns:
        html: template that lists states, cities & amenity sort by name A->Z
    """
    data = {
        "states": storage.all("State").values(),
        "places": storage.all("Place").values(),
        "amenities": storage.all("Amenity").values()
    }
    return render_template("100-hbnb.html", models=data)


@app.teardown_appcontext
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
