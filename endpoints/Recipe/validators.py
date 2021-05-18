from flask_restful import reqparse


def recipe_post_validator():
    recipe_post_args = reqparse.RequestParser()
    recipe_post_args.add_argument("name", type=str, help="Name of recipe is required", required=True)
    recipe_post_args.add_argument("ingredient", type=str, help="ingredient needs to be string and it is required",
                                  required=True)
    recipe_post_args.add_argument("unit", type=str, help="unit needs to be string and it is required", required=True)
    recipe_post_args.add_argument("qty", type=int, help="qty needs to be int and it is required", required=True)
    return recipe_post_args
