from flask import url_for
from flask_testing import TestCase
from applications import models, app
from applications.models import Users, Recipes
from applications import app, db 

class TestBase(TestCase):
    def create_app(self):
        app.config.update( SQLALCHEMY_DATABASE_URI="sqlite:///",
        SECRET_KEY = 'TEST_SECRET_KEY',
        DEBUG = True,
        WTF_CSRD_ENABLE = False
        )
        return app

    def setUp(self):
        db.create_all()
        sample1 = Users(first_name="Bob",
        last_name = "Roberts",
        email = "bobroberts@hotmail.com",
        phone_number = "07912345678")

        db.session.add(sample1)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):
    def test_get_home(self):
        response = self.client.get(url_for('read'))
        self.assert200(response,"Failed to load read page")

class TestViews(TestBase):
    def test_get_read(self):
        response = self.client.get(url_for('readusers'))
        self.assert200(response,"Failed to load ReadUsers page")

class TestViews(TestBase):
    def test_get_signup(self):
        response = self.client.get(url_for('signup'))
        self.assert200(response,"Failed to load signup page")







