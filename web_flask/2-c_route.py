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
    /c/<text>: Displays 'C' followed by the value of <text>.
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
    return "HBNB"

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
    return "HBNB"
>>>>>>> fbc8b3ff7d981ae766ee7c2a86ad1ace0f06995f

@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Displays 'C' followed by the value of <text>."""
    text = text.replace("_", " ")
    return "C {}".format(text)

<<<<<<< HEAD

if __name__ == "__main__":
    app.run(host="0.0.0.0")
=======
@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """
    display “C ” followed by the value of the text variable
        (replace underscore '_' symbols with a space ' ')
    Returns:
        str: "C <text>"
    """
    return "C {}".format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
>>>>>>> fbc8b3ff7d981ae766ee7c2a86ad1ace0f06995f
