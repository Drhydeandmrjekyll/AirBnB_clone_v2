#!/usr/bin/python3
""" Start Flash Web Application HBNB"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Print message when / is called """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Prints Message when /hbnb is called """
    return 'HBNB'

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
