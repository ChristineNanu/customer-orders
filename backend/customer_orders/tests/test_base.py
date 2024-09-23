from django.contrib.auth import get_user_model
from rest_framework.test import APIClient, APITestCase

TEST_CLIENT_USERNAME = "test_user"


class BaseTestCase(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.loggedin_client = APIClient()
        client_user, _ = get_user_model().objects.get_or_create(
            username=TEST_CLIENT_USERNAME
        )
        cls.loggedin_client.force_authenticate(user=client_user)

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        get_user_model().objects.filter(username=TEST_CLIENT_USERNAME).delete()
