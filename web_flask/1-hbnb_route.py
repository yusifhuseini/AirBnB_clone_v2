#!/usr/bin/python3
<<<<<<< HEAD
"""Starts a Flask web application.
=======
"""
A script that starts a Flask web application:
"""
>>>>>>> fbc8b3ff7d981ae766ee7c2a86ad1ace0f06995f

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'.
    /hbnb: Displays 'HBNB'.
"""
from flask import Flask

app = Flask(__name__)


<<<<<<< HEAD
@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays 'HBNB'."""
=======
@app.route('/', strict_slashes=False)
def hello_route():
    """
    Displays 'Hello HBNB!'
    Returns:
        str: "Hello HBNB"
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    """
    Displays 'HBNB'
    Returns:
        str: "HBNB"
    """
>>>>>>> fbc8b3ff7d981ae766ee7c2a86ad1ace0f06995f
    return "HBNB"


if __name__ == "__main__":
<<<<<<< HEAD
    app.run(host="0.0.0.0")
=======
    app.run(host="0.0.0.0", port=5000)
>>>>>>> fbc8b3ff7d981ae766ee7c2a86ad1ace0f06995f
