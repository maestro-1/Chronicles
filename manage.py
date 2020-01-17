import unittest
from flaskblog import app
from flask_script import Manager

manager = Manager(app)


@manager.command
def tests():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)


if __name__ == '__main__':
    manager.run()
