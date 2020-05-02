from tests.test_basic import BaseTestCase
import unittest
# from flaskblog.models import User


class BasicTestsCase(BaseTestCase):
  def test_correct_signUp(self):
    response = self.client.post('/register',
                                data=dict(username='maestro',
                                          email='marho219@gmail.com',
                                          password='#IlovePapi',
                                          confirm_password='#IlovePapi'),
                                follow_redirects=True
                                )
    self.assert_template_used('register.html')
    self.assertNotEqual(response.data.decode('utf-8').find('marho219@gmail.com'), None)
    # user = User.query.filter_by(email='marho219@gmail.com').first()
    # self.assertTrue(user.username == 'maestro')

  def test_password_too_short(self):
    response = self.client.post('/register',
                                data=dict(username='uzezi',
                                          email='ruon85@gmail.com',
                                          password='#I lo',
                                          confirm_password='#I lo'),
                                follow_redirects=True
                                )
    self.assertIn(b'<span>Field must be between 8 and 20 characters long.</span>',
                  response.data)

  def test_email_already_in_use(self):
    response = self.client.post('/register',
                                data=dict(username='uzezi',
                                          email='ruon85@gmail.com',
                                          password='#I love papi',
                                          confirm_password='#I love papi'),
                                follow_redirects=True
                                )
    self.assertIn(b'<span>email already in use try a different email address</span>',
                  response.data)

  def test_username_already_used(self):
    response = self.client.post('/register',
                                data=dict(username='eye candy',
                                          email='ruon85@gmail.com',
                                          password='#I love papi',
                                          confirm_password='#I love papi'),
                                follow_redirects=True
                                )
    self.assertIn(b'<span>username already taken try a different username</span>',
                  response.data)

  def test_password_do_not_match(self):
    response = self.client.post('/register',
                                data=dict(username='uzezi',
                                          email='ruon85@gmail.com',
                                          password='#I love papi',
                                          confirm_password='#I love mama'),
                                follow_redirects=True
                                )
    self.assertIn(b'<span>Field must be equal to password.</span>',
                  response.data)


if __name__ == '__main__':
  unittest.main()
