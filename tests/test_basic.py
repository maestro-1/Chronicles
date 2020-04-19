from flask_testing import TestCase
from flaskblog import db, app
from flaskblog.models import User, Post


class BaseTestCase(TestCase):
    def create_app(self):
        app.config['SECRET_KEY'] = 'ed576332c78752f352dc0936gp34945b'
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        return app

    # @classmethod
    def setUp(self):
        db.create_all()
        db.session.add(User(username='eye of ron', email='ruon85@gmail.com',
                            password='valeria@31'))
        db.session.add(User(username='eye candy', email='beauty@gmail.com',
                            password='32nwankwo@beautiful'))
        db.session.commit()
        author1 = User.query.get(1)
        author2 = User.query.get(2)
        db.session.add(Post(title='cinematography',
                            content='The concept of cinematography is quite easty to be sincere',
                            author=author1))
        db.session.add(Post(title='fashion design',
                            content='fashion design is a misunderstood concept, one i will attempt to rectiy',
                            author=author2))
        db.session.commit()

    # @classmethod
    def tearDown(self):
        db.session.remove()
        db.drop_all()
