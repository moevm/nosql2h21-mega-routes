from flask import jsonify
from flask_restful import Resource

from web_app.db.models import WayNode
class AnalyticsApi(Resource):
    def get(self):
        pass