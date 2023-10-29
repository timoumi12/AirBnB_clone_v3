#!/usr/bin/python3
"""index.py file"""
from flask import jsonify
from api.v1.views import app_views
from models import storage
from models.amenity import Amenity
from models.review import Review
from models.user import User
from models.city import City
from models.state import State
from models.place import Place


@app_views.route('/status')
def index():
    """returns OK"""
    status = {"status": "OK"}
    return jsonify(status)


@app_views.route('/stats')
def _count():
    stats = {"Amenity": storage.count(Amenity),
               "City": storage.count(City),
               "Place": storage.count(Place),
               "Review": storage.count(Review),
               "State": storage.count(State),
               "User": storage.count(User)}
    return jsonify(stats)
