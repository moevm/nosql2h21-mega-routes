from flask import Response, current_app, jsonify, make_response, request
from flask_restful import Resource

from web_app.db.models import WayNode
class MapsApi(Resource):
    def post(self):
        pass