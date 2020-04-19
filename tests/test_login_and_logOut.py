from tests.test_basic import BaseTestCase
import unittest
from flask_login import current_user
from flaskblog.models import User


class BasicTestsCase(BaseTestCase):
    def test_correct_login_1(self):
        with self.client:
            self.client.post(
                '/login',
                data=dict(username='eye of ron', password='valeria@31'),
            )
            self.assert_template_used('login.html')
            user1 = User.query.get(1)
            self.assertEqual('eye of ron', user1.username)
            self.assertEqual(user1.password, 'valeria@31')
            self.assertNotEqual(user1.password, 'millies')

    def test_correct_login_2(self):
        with self.client:
            self.client.post(
                '/login',
                data=dict(username='eye of ron', password='valeria@31'),
            )
            self.assert_template_used('login.html')
            user2 = User.query.get(2)
            self.assertEqual('eye candy', user2.username)
            self.assertNotEqual(user2.password, 'valeria@31')

    def test_wrong_login(self):
        with self.client:
            response = self.client.post(
                '/login',
                data=dict(username='millies', password='admin')
            )
            self.assert200(response)
            self.assertIn(b'<legend class="border-bottom mb-4">Log In</legend>',
                          response.data)
            self.assertIn(b'<label class="form-check-label" for="remember">Remember Me</label>',
                          response.data)
            self.assert_template_used('login.html')

    def test_logout(self):
        with self.client:
            response = self.client.get('/logout')
            self.assert_redirects(response=response, location='/')
            self.assertFalse(current_user.is_authenticated)


if __name__ == '__main__':
    unittest.main()
