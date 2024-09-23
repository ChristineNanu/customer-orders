from customer_orders.tests.test_base import BaseTestCase
from customers.models import Customer
from django.urls import reverse
from rest_framework import status


class CustomerAPITests(BaseTestCase):
    def setUp(self):
        customer_data = {
            "name": "Musa",
            "code": "CUST.001",
            "mobile_number": "+254711111111",
        }
        self.customer = Customer.objects.create(**customer_data)

    def test_create_customer(self):
        customer_data = {
            "name": "Chebet",
            "code": "CUST.002",
            "mobile_number": "+254722222222",
        }
        response = self.loggedin_client.post(
            reverse("customer_list_create"), customer_data
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customer.objects.count(), 2)

    def test_list_customers(self):
        response = self.loggedin_client.get(reverse("customer_list_create"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_customer(self):
        response = self.loggedin_client.get(
            reverse("customer_detail", args=[self.customer.id])
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], self.customer.name)

    def test_update_customer(self):
        updated_data = {"name": "Ali"}
        response = self.loggedin_client.patch(
            reverse("customer_detail", args=[self.customer.id]), updated_data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.customer.refresh_from_db()
        self.assertEqual(self.customer.name, "Ali")

    def test_delete_customer(self):
        response = self.loggedin_client.delete(
            reverse("customer_detail", args=[self.customer.id])
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Customer.objects.count(), 0)
