#!/usr/bin/python3
"This script for start flask"
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hbnbhome():
    "this fun for display “Hello HBNB!”"
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def displayhbnb():
    "this fun for display hbnb"
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    "this fuc for display C fllowed by text"
    txt = text.replace('_', ' ')
    return f"C {txt}"


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text_var(text):
    "this fun for display python followed by text "
    txt = text.replace('_', ' ')
    return f"Python {txt}"


@app.route('/number/<int:n>', strict_slashes=False)
def number_int(n):
    "this func for return number int"
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    "this func for display a HTML page only if n is an integer"
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    "odd even"
    odd_or_even = "even" if n % 2 == 0 else "odd"
    return render_template('6-number_odd_or_even.html', n=n,
                           odd_or_even=odd_or_even)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
