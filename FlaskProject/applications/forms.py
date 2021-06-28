from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, IntegerField
from wtforms.validators import DataRequired, ValidationError, Email 
from os import getenv


class SignUpForm(FlaskForm):
    first_name = StringField('First Name: ', validators = [DataRequired()])
    last_name = StringField('Last Name: ', validators = [DataRequired()])
    email = StringField('Email Address: ', validators = [Email()])
    phone_number = StringField('Phone number: ', validators = [DataRequired()])
    submit = SubmitField('Add User')
    
class RecipeForm(FlaskForm):
    recipe_name = StringField('Recipe Name: ', validators = [DataRequired()]) 
    ingredients = StringField('Ingredients used: ', validators = [DataRequired()])
    instructions = StringField('Cooking Instructions: ', validators = [DataRequired()])
    submit = SubmitField('Add Recipe')


