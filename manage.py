import unittest
from flaskblog import app
from flask_script import Manager
from flaskblog.models import User, Post
from flaskblog import db

manager = Manager(app)


@manager.command
def tests():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@manager.command
def create_tables():
    db.create_all()


@manager.command
def delete_tables():
    db.drop_all()


if __name__ == '__main__':
    manager.run()
