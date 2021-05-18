from shared.request.response import generic_response
from endpoints.Recipe.models import Recipe
from shared.utils import save_one_record

recipes = {}


def add_recipe_service(incoming):
    recipe = Recipe(name=incoming["name"], ingredient=incoming["ingredient"], unit=incoming["unit"], qty=incoming["qty"])
    save_one_record(record=recipe)
    return generic_response(status_code=201, success=True, message="Recipe added successfully", data=incoming)


def get_recipe_service(recipe_id):
    if recipe_id in recipes:
        data = recipes[recipe_id]
        return generic_response(status_code=200, success=True, message="Recipe found successfully", data=data)
    else:
        return generic_response(status_code=404, success=False, message="Recipe doesn't exist")
