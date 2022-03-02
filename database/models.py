from .db import db

class Recipes(db.Document): 
    name = db.Stringfield(required=True, unique=True)
    cuisine_type = db.Stringfield(required=True)
    description = db.Stringfield(required=True)
    image = db.Stringfield (required=True)
    ingredient_one = db.Stringfield(required=True)
    ingredient_two = db.Stringfield(required=False)
    ingredient_three = db.Stringfield(required=False)
    ingredient_four = db.Stringfield(required=False)
    ingredient_five = db.Stringfield(required=False)
    ingredient_six = db.Stringfield(required=False)
    ingredient_seven = db.Stringfield(required=False)
    directions = db.Stringfield(required =True)