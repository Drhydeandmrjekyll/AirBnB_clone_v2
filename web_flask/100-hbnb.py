#!/usr/bin/python3
"""100-hbnb.py"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
import os

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.teardown_appcontext
def close_db(error):
    """Closes the database again at end of request."""
    storage.close()

@app.route('/hbnb', methods=['GET'])
def hbnb():
    """Display HTML page like 8-index.html"""
    states = storage.all(State).values()
    cities = storage.all(City).values()
    amenities = storage.all(Amenity).values()
    places = storage.all(Place).values()

    states = sorted(states, key=lambda state: state.name)
    cities = sorted(cities, key=lambda city: city.name)
    amenities = sorted(amenities, key=lambda amenity: amenity.name)
    places = sorted(places, key=lambda place: place.name)

    return render_template('100-hbnb.html', states=states, cities=cities, amenities=amenities, places=places)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
