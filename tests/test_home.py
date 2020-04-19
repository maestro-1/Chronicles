from tests.test_basic import BaseTestCase
import unittest


class HomeTestsCase(BaseTestCase):
    def test_home_page(self):
        # pass
        response = self.client.get('/')
        self.assert_template_used('home.html')
        self.assert200(response)

    def test_about_page(self):
        response = self.client.get('/about')
        self.assert_template_used('about.html')
        self.assert200(response)


if __name__ == '__main__':
    unittest.main()
