from flask_restful import Resource
from endpoints.Recipe.services import add_recipe_service, get_recipe_service
from endpoints.Recipe.validators import recipe_post_validator


class RecipeList(Resource):

    def post(self):
        validator = recipe_post_validator()
        args = validator.parse_args()
        return add_recipe_service(incoming=args)


class RecipeDescription(Resource):

    def get(self, recipe_id):
        return get_recipe_service(recipe_id=recipe_id)
