from .recipe import RecipesApi

def initialize_routes(api):
    api.add_resource(RecipesApi, '/api/recipies')