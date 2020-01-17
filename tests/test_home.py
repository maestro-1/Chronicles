from tests.base import BaseTestCase


class HomeTestsCase(BaseTestCase):
    def test_home_route(self):
        assert_template_used('home.html')
        # print('done')
