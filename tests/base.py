from flask import Flask
from flask_test import TestCase
from flaskblog import db
# from flaskblog.models import User, Post


class BaseTestCase(TestCase):
    def create_app():
        app = Flask(__name__)
        app.config['SECRET_KEY'] = 'ed576332c78752f352dc0936gp34945b'
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        return app

    def setUp():
        db.create_all()
        # db.session.add(User(username='eye of ron', email='ruon85@gmail.com', password='valeria@31'))
        # db.session.add(User(username='eye candy', email='beauty@gmail.com', password='32nwankwo@beautiful'))
        # db.session.add(Post(title='cinematography', content='The concept of cinematography is quite easty to be sincere'))
        # db.session.commit()

    def tearDown():
        db.session.remove()
        db.drop_all()
