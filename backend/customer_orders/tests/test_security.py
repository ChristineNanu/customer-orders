from django.urls import reverse
from rest_framework import status

from .test_base import BaseTestCase


class SecurityHeadersMiddlewareTest(BaseTestCase):
    def test_security_headers(self):
        response = self.client.get(reverse("customer_list_create"))

        self.assertEqual(response["X-Content-Type-Options"], "nosniff")
        self.assertEqual(
            response["Strict-Transport-Security"], "max-age=31536000; includeSubDomains"
        )
        self.assertEqual(response["Referrer-Policy"], "no-referrer-when-downgrade")


class APIPermissionsTest(BaseTestCase):
    def test_authorized_access(self):
        response = self.loggedin_client.get(reverse("customer_list_create"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthorized_access(self):
        response = self.client.get(reverse("customer_list_create"))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
