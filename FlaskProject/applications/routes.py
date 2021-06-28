from applications import app, db
from applications.models import Recipes, Users
from applications.forms import SignUpForm, RecipeForm, request, render_template, redirect, url_for

@app.route('/', methods = ['GET'])
@app.route('/home', methods = ['GET'])
def Title():
    return render_template('home.html')

@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    error = ""
    form = SignUpForm()

    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        phone_number = form.phone_number.data

        if len(first_name) == 0 or len(last_name) == 0:
            error = "Please supply first and last name "
        elif len(email) == 0:
            error = "Please supply an email address"
        elif len(phone_number) == 0:
            error = "Please supply a phone number "
        else:  
            enter = Users(first_name = first_name, last_name = last_name, email = email, phone_number = phone_number)
            db.session.add(enter)
            db.session.commit()
            return f'Thank you {first_name} {last_name}'
    return render_template('signup.html', form = form, message = error)

@app.route('/add', methods = ['GET', 'POST'])
def addrecipe():
    error = ""
    form = RecipeForm()

    if request.method == 'POST':
        recipe_name = form.recipe_name.data
        ingredients = form.ingredients.data
        instructions = form.instructions.data

        if len(recipe_name) == 0:
            error = "Please supply recipe name"
        elif len(ingredients) == 0:
            error = "Please supply list of ingredients"
        elif len(instructions) == 0:
            error = "Please supply instructions" 

        else:
            recipeenter = Recipes(recipe_name = recipe_name, ingredients = ingredients, instructions = instructions)
            db.session.add(recipeenter)
            db.session.commit()
            return 'Recipe Added'
    return render_template('add.html', form = form, message = error)
    
@app.route('/read', methods = ['GET'])
def read():
    if request.method == 'GET':
        all_recipes = Recipes.query.all()
        recipe_string= ""
        for recipe in all_recipes:
            recipe_string += "<br>"+ recipe.recipe_name
    return recipe_string

@app.route('/readusers', methods = ['GET'])
def readuser():
    if request.method == 'GET':
        all_users = Users.query.all()
        users_string = ""
        for user in all_users:
            users_string += "<br>" + user.first_name
    return users_string

@app.route('/updateuser/<first_name>',methods = ['GET', 'POST'])
def update(first_name):
    first_user = Users.query.first()
    first_user.first_name = first_name
    db.session.commit()
    return first_user.first_name
  

@app.route('/updaterecipe/<recipe_name>',methods = ['GET', 'POST'])
def updaterecipe(recipe_name):
    first_recipe = Recipes.query.first()
    first_recipe.recipe_name = recipe_name
    db.session.commit()
    return first_recipe.recipe_name
    
@app.route('/delete')
def delete():
    recipe_delete = Recipes.query.first()
    db.session.delete(recipe_delete)
    db.session.commit()
    return 'Recipe deleted'

@app.route('/deleteuser')
def deleteuser():
    user_delete = Users.query.first()
    db.session.delete(user_delete)
    db.session.commit()
    return 'User deleted'