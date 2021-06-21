from applications import db


class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key= True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(150), unique = True)
    phone_number = db.Column(db.String(12))
    verified = db.Column(db.Boolean, default= False)



class Recipes(db.Model):
    recipe_id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(30))
    date_posted = db.Column(db.DateTime)
    total_time_taken = db.Column(db.String(20))
    ingredients = db.Column(db.String(500))
    instrunctions = db.Column(db.String(2000))
    user_id = db.Column(db.Integer, db.ForeignKey(Users.user_id))

    
