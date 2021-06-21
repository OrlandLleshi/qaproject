from applications import app, db
from applications.models import Recipes


@app.route('/')
@app.route('/home')
def Title():
    return 'Recipe App!'

@app.route('/about')
def about():
    return 'This is the about page'

@app.route('/recipe')
def recipe():
    return 'This is the recipe page'

@app.route('/update')
def update():
    return 'This is the update page'

@app.route('/delete')
def delete():
    return 'This is the delete page'