from flask import Blueprint
from flask_restful import Api
from resources.search import Search
from resources.words import Words

# Making a flask blueprint
api_blueprint = Blueprint('dictionary-api', __name__)

api = Api(api_blueprint)

api.add_resource(Search, '/search')
api.add_resource(Words, '/words/<string:word>')
