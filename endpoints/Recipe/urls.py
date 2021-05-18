from endpoints.Recipe.views import RecipeList, RecipeDescription
from shared.services.config import get_configs

configs = get_configs()


def recipe_urls(api):
    base = configs['api']['base']
    recipe_uri = configs['api']['Recipe']['uri']

    api.add_resource(RecipeList, base + recipe_uri)
    api.add_resource(RecipeDescription, base + recipe_uri + '/<int:recipe_id>')
