from tests.test_basic import BaseTestCase
import unittest
from flask_login import current_user
from flaskblog.models import User


class BasicTestsCase(BaseTestCase):
    def test_first_correct_login_1(self):
        with self.client:
            response = self.client.post(
                '/login',
                content_type='multipart/form-data',
                data=dict(email='ruon85@gmail.com', password='valeria@31')
                # follow_redirects=True
            )
            self.assert_template_used('login.html')
            print(current_user.is_authenticated)

#     def test_second_correct_login(self):
#         with self.client:
#             self.client.post(
#                 '/login',
#                 data=dict(username='eye of ron', password='valeria@31'),
#             )
#             self.assert_template_used('login.html')
#             user2 = User.query.get(2)
#             self.assertEqual('eye candy', user2.username)
#             self.assertNotEqual(user2.password, 'valeria@31')

#     def test_invalid_username_login(self):
#         with self.client:
#             response = self.client.post(
#                 '/login',
#                 data=dict(username='millies', password='admin')
#             )
#             user = User.query.filter_by(username='millies').first()
#             self.assertEqual(user, None)

#     def test_logout(self):
#         with self.client:
#             response = self.client.get('/logout')
#             self.assert_redirects(response=response, location='/')
#             self.assertFalse(current_user.is_authenticated)


# if __name__ == '__main__':
#     unittest.main()
