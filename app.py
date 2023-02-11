from flask import Flask, jsonify
import requests
from flask_restful import Api, Resource, reqparse
from bs4 import BeautifulSoup
import json
import soup
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)

class Leetcode(Resource):
    @staticmethod
    def get(username):
        return soup.Data(username).get_details()

leetcode = Leetcode()
api.add_resource(Leetcode, "/<string:username>")

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')