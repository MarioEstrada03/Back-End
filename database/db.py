from flask_mongonegine import MongoEngine

db = MongoEngine()

def initialize_db(app):
    db.init_app(app)