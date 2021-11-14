from flask import Response, request, current_app
from flask_restful import Resource


class MapsApi(Resource):
    def post(self):
        try:
            start = request.get_json()["start"]
            end = request.get_json()["end"]
            # bla bla bla
            return Response(status=200)
        except TypeError:
            current_app.logger.exception("Received invalid JSON file!")
            return Response("Invalid JSON file!", status=403)
