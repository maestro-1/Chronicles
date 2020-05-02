from tests.test_basic import BaseTestCase
import unittest


class BasicTestsCase(BaseTestCase):
    def test_user_posts(self):
        with self.client:
            response = self.client.get('/user/eye candy')
            self.assert_template_used('users_page.html')
            self.assert200(response)
            self.assertIn(b'<h1 class="mb-3">Posts by eye candy (1)</h1>', response.data)


if __name__ == '__main__':
    unittest.main()
