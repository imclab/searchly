from app import app, api
from website.views import *
from users.endpoints import *

API_URL = '/api/v1/'


#urls
def initialize_urls():
    #Add initial url
    app.add_url_rule('/', 'index', index, methods=['GET'])

    #add rest api endpoints
    api.add_resource(Users, API_URL + 'users', endpoint='users')