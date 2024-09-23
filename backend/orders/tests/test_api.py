from customer_orders.tests.test_base import BaseTestCase
from customers.models import Customer
from django.urls import reverse
from orders.models import Order
from rest_framework import status


class OrderAPITests(BaseTestCase):
    def setUp(self):
        self.customer = Customer.objects.create(
            name="Musa", code="CUST.001", mobile_number="+254711111111"
        )
        self.order = Order.objects.create(
            customer=self.customer, item="Cake", amount=1925.50
        )

    def test_create_order(self):
        order_data = {
            "customer": self.customer.id,
            "item": "Cake",
            "amount": 1925.50,
        }
        response = self.loggedin_client.post(reverse("order_list_create"), order_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 2)

    def test_list_orders(self):
        response = self.loggedin_client.get(reverse("order_list_create"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_order(self):
        response = self.loggedin_client.get(
            reverse("order_detail", args=[self.order.id])
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["item"], self.order.item)

    def test_update_order(self):
        updated_data = {"item": "Muffin"}
        response = self.loggedin_client.patch(
            reverse("order_detail", args=[self.order.id]), updated_data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.order.refresh_from_db()
        self.assertEqual(self.order.item, "Muffin")

    def test_delete_order(self):
        response = self.loggedin_client.delete(
            reverse("order_detail", args=[self.order.id])
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Order.objects.count(), 0)
