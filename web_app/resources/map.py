from flask import Response, request, current_app, jsonify
from flask_restful import Resource


class MapsApi(Resource):
    def post(self):
        try:
            start = request.get_json()["start"]
            finish = request.get_json()["finish"]
            return Response(start+' '+finish, status=200)
        except TypeError:
            current_app.logger.exception("Received invalid JSON file!")
            return Response("Invalid JSON file!", status=403)
