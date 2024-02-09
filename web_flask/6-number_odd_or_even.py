#!/usr/bin/python3
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'.
    /hbnb: Displays 'HBNB'.
    /c/<text>: Displays 'C' followed by the value of <text>.
    /python/(<text>): Displays 'Python' followed by the value of <text>.
    /number/<n>: Displays 'n is a number' only if <n> is an integer.
    /number_template/<n>: Displays an HTML page only if <n> is an integer.
        - Displays the value of <n> in the body.
    /number_odd_or_even/<n>: Displays an HTML page only if <n> is an integer.
        - States whether <n> is even or odd in the body.
"""
<<<<<<< HEAD
from flask import Flask
from flask import render_template

=======
A script that starts a Flask web application:
"""

from flask import Flask
from flask import render_template

>>>>>>> fbc8b3ff7d981ae766ee7c2a86ad1ace0f06995f
app = Flask(__name__)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


<<<<<<< HEAD
@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays 'HBNB'"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Displays 'C' followed by the value of <text>

    Replaces any underscores in <text> with slashes.
    """
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """Displays 'Python' followed by the value of <text>
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

    Replaces any underscores in <text> with slashes.
    """
    text = text.replace("_", " ")
    return "Python {}".format(text)

<<<<<<< HEAD
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
>>>>>>> fbc8b3ff7d981ae766ee7c2a86ad1ace0f06995f

@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Displays 'n is a number' only if <n> is an integer."""
    return "{} is a number".format(n)

<<<<<<< HEAD
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
>>>>>>> fbc8b3ff7d981ae766ee7c2a86ad1ace0f06995f

@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Displays an HTML page only if <n> is an integer.

<<<<<<< HEAD
    Displays the value of <n> in the body.
    """
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """Displays an HTML page only if <n> is an integer.
=======
@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """
    display “n is a number” only if n is an integer
    Returns:
        int: the value of n
    """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template_route(n):
    """
    display a HTML page only if n is an integer:
        H1 tag: “Number: n” inside the tag BODY
    Returns:
        html: template displaying the value of n
    """
    return render_template('5-number.html', n=n)
>>>>>>> fbc8b3ff7d981ae766ee7c2a86ad1ace0f06995f

    States whether <n> is odd or even in the body.
    """
    return render_template("6-number_odd_or_even.html", n=n)

<<<<<<< HEAD

if __name__ == "__main__":
    app.run(host="0.0.0.0")
=======
@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even_route(n):
    """
    display a HTML page only if n is an integer:
        H1 tag: “Number: n is even|odd” inside the tag BODY
    Returns:
        html: template displaying the value of n stating if even or odd
    """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
>>>>>>> fbc8b3ff7d981ae766ee7c2a86ad1ace0f06995f
