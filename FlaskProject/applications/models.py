from applications import db


class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key= True, nullable = False)
    first_name = db.Column(db.String(50), nullable = False)
    last_name = db.Column(db.String(50), nullable = False)
    email = db.Column(db.String(150), unique = True, nullable = False)
    phone_number = db.Column(db.String(12), unique = True, nullable = False)
    recipes = db.relationship('Recipes', backref = 'user')



class Recipes(db.Model):
    recipe_id = db.Column(db.Integer, primary_key=True, nullable = False)
    recipe_name = db.Column(db.String(30), nullable = False)
    ingredients = db.Column(db.String(500), nullable = False)
    instructions = db.Column(db.String(2000), nullable = False)
    id = db.Column(db.Integer, db.ForeignKey(Users.user_id))

    
