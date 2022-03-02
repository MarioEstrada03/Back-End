from flask import Response, request
from database.models import Recipes
from flask_restful import Resource


# Get
class RecipesApi(Resource):
    def get(self):
        recipes = Recipe.objects().to_json()
        return Response(
            recipes,
            minetype = "application/json"
        )
# Create
    def post(self):
        body = request.get_json()
        recipe = Recipe(**body).save()
        id = recipe.id
        return {"id": str(id)}
# Update

# Delete