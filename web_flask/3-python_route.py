#!/usr/bin/python3
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'.
    /hbnb: Displays 'HBNB'.
    /c/<text>: Displays 'C' followed by the value of <text>.
    /python/(<text>): Displays 'Python' followed by the value of <text>.
"""
<<<<<<< HEAD
=======
A script that starts a Flask web application:
"""

>>>>>>> fbc8b3ff7d981ae766ee7c2a86ad1ace0f06995f
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


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Displays 'C' followed by the value of <text>.

    Replaces any underscores in <text> with slashes.
    """
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """Displays 'Python' followed by the value of <text>.
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


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """
    display “C ” followed by the value of the text variable
        (replace underscore '_' symbols with a space ' ')
    Returns:
        str: "C <text>"
    """
    return "C {}".format(text.replace('_', ' '))
>>>>>>> fbc8b3ff7d981ae766ee7c2a86ad1ace0f06995f

    Replaces any underscores in <text> with slashes.
    """
    text = text.replace("_", " ")
    return "Python {}".format(text)

<<<<<<< HEAD

if __name__ == "__main__":
    app.run(host="0.0.0.0")
=======
@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text="is_cool"):
    """
    display “Python ”, followed by the value of the text variable
        (replace underscore _ symbols with a space )
        - The default value of text is “is cool”
    Returns:
        str: "Python <text>"
    """
    return "Python {}".format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
>>>>>>> fbc8b3ff7d981ae766ee7c2a86ad1ace0f06995f
