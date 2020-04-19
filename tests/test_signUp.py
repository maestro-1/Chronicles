from tests.test_basic import BaseTestCase
import unittest


class BasicTestsCase(BaseTestCase):
    def test_correct_signUp(self):
        with self.client:
            response = self.client.post('/register',
                                        data=dict(username='maestro',
                                                  email='marho219@gmail.com',
                                                  password='#I love papi',
                                                  confirm_password='#I love papi'),
                                        follow_redirects=True
                                        )
            self.assert_template_used('register.html')

    def test_password_too_short(self):
        pass

    def test_email_already_in_use(self):
        pass

    def test_username_already_in_use(self):
        pass


if __name__ == '__main__':
    unittest.main()
