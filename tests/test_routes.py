from flask_testing import TestCase
from application.models import Users 
from application import app, db
from flask import render_template, redirect, url_for, request


class TestBase(TestCase):

    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI='sqlite:///data.db', DEBUG=True, WTF_CSRF_ENABLED=False)
        return app

    def setUp(self):
        db.create_all()

        test_User = Users(user_name="Vicky_Jones", loans=1000, password="Groovy123", property=1000000, cash=500000, investments=200000)

        db.session.add(test_User)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    
class TestViews(TestBase):

    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_add_profile(self):
        response = self.client.get(url_for('add_profile'))
        self.assertEqual(response.status_code, 200)

    def test_add_profile(self):
        response = self.client.get(url_for('add_debt'))
        self.assertEqual(response.status_code, 200)

    def test_add_profile(self):
        response = self.client.get(url_for('update_profile', 1))
        self.assertEqual(response.status_code, 302)


    def test_add_profile(self):
        response = self.client.get(url_for('update_debt', 1))
        self.assertEqual(response.status_code, 302)

    def test_add_profile(self):
        response = self.client.get(url_for('view_networth', 1))
        self.assertEqual(response.status_code, 302)    

    def test_add_profile(self):
        response = self.client.get(url_for('delete_profile', 1))
        self.assertEqual(response.status_code, 302)






