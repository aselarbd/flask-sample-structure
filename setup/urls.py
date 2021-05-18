from flask_restful import Api
from endpoints.Recipe.urls import recipe_urls


class MainURLRegister:
    api_ref = None

    def __init__(self, app):
        api = Api(app)
        MainURLRegister.api_ref = api
        recipe_urls(api=api)
