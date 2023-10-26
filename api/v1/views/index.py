#!/usr/bin/python3
"""index.py file"""
from flask import jsonify
from api.v1.views import app_views

@app_views.route('/status')
def index():
    """returns OK"""
    status = {"status": "OK"}
    return jsonify(status)
