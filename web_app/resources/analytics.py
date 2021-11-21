from flask import jsonify
from flask_restful import Resource


class AnalyticsApi(Resource):
    def get(self):
        return jsonify({'a': 'a'})
