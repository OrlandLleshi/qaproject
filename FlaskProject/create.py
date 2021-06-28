from applications import db
from applications.models import Users, Recipes 


db.drop_all()
db.create_all()