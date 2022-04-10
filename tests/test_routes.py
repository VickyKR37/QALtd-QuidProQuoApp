from application.models import Users, Loans
from flask_testing import TestCase
from application import app, db
from flask import url_for
from flask_testing import LiveServerTestCase

class TestBase(TestCase):

    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI='sqlite:///data.db', DEBUG=True, WTF_CSRF_ENABLED=False)
        return app

    def setUp(self):
        db.create_all()
        
        test_user = Users(user_name="Vicky_Jones", password="Groovy123", property=1000000, cash=500000, investments=200000)
       
        db.session.add(test_user)
        db.session.commit()

        test_loan = Loans(user_id=1, amount_borrowed=1000, lender_id="Halifax")
        
        db.session.add(test_loan)
        db.session.commit()


    def tearDown(self):
        db.session.remove()
        db.drop_all()

# #testing the URL endpoints for all routes:    
class TestViews(TestBase):

    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_add_profile(self):
        response = self.client.get(url_for('add_profile'))
        self.assertEqual(response.status_code, 200)

    def test_add_debt(self):
        response = self.client.get(url_for('add_debt'))
        self.assertEqual(response.status_code, 200)

    def test_update_profile(self):
        response = self.client.get(url_for('update_profile', user_id = 1))
        self.assertEqual(response.status_code, 200)


    def test_update_debt(self):
        response = self.client.get(url_for('update_debt', user_id = 1))
        self.assertEqual(response.status_code, 200)

    def test_view_networth(self):
        response = self.client.get(url_for('view_networth', user_id = 1))
        self.assertEqual(response.status_code, 200)    

    def test_delete_profile(self):
        response = self.client.get(url_for('delete_profile', user_id = 1))
        self.assertEqual(response.status_code, 302)

    def test_post_req(self):
        response = self.client.post(url_for('add_profile'), data = dict(user_name="Vicky_Rai", password="Groovy123", property=1000000, cash=500000, investments=200000))
        self.assertIn(b'Create', response.data)


# Integration testing (testing the database)
class TestData(TestBase):

    def check_name(self):
        response = test_user.query.first()
        self.assertIn("Vicky_Jones", response.data.decode)

    

