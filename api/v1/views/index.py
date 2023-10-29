#!/usr/bin/python3
"""index.py file"""
from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status')
def index():
    """returns OK"""
    status = {"status": "OK"}
    return jsonify(status)


@app_views.route('/stats')
def _count():
    stats = {
        "amenities": storage.count()
    }
