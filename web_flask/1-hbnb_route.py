#!/usr/bin/python3
"This script for start flask"
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hbnbhome():
    "this fun for display “Hello HBNB!”"
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def displayhbnb():
    "this fun for display hbnb"
    return "HBNB"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
