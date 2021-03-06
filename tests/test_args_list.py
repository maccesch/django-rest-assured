from rest_assured.testcases import ListAPITestCaseMixin
from tests import mocks


class TestListTestCase:
    def get_case(self, **kwargs):
        class MockListTestCase(ListAPITestCaseMixin, mocks.MockTestCase):
            base_name = 'stuff_with_param'
            factory_class = mocks.StuffFactory
            reverse_args = ["foobar", 42]

        self.case_class = MockListTestCase

        return MockListTestCase(**kwargs)

    def test_get_list_url(self):
        instance = self.get_case(methodName='dummy')
        instance.setUp()
        assert instance.get_list_url() == '/stuff/with/foobar/42/'

    def test_get_list_response(self):
        instance = self.get_case(methodName='dummy')
        instance.setUp()
        response = instance.get_list_response()
        assert response
        assert response.status_code == 200
        assert response.data

    def test_test_list(self):
        instance = self.get_case(methodName='dummy')
        instance.setUp()
        response = instance.test_list()
        assert response
