from rest_assured.testcases import DestroyAPITestCaseMixin
from tests import mocks


class TestDestroyTestCase:
    def get_case(self, **kwargs):
        class MockDestroyTestCase(DestroyAPITestCaseMixin, mocks.MockTestCase):
            base_name = 'stuff_with_param'
            factory_class = mocks.StuffFactory
            reverse_args = ["foobar", 42]

        self.case_class = MockDestroyTestCase

        return MockDestroyTestCase(**kwargs)

    def test_get_destroy_url(self):
        instance = self.get_case(methodName='dummy')
        instance.setUp()
        assert instance.get_destroy_url() == '/stuff/with/foobar/42/%s/' % instance.object.pk

    def test_get_destroy_response(self):
        instance = self.get_case(methodName='dummy')
        instance.setUp()
        response = instance.get_destroy_response()
        assert response
        assert response.status_code == 204

    def test_test_destroy(self):
        instance = self.get_case(methodName='dummy')
        instance.setUp()
        response = instance.test_destroy()
        assert response
