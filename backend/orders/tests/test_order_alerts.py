from unittest.mock import patch

from customers.models import Customer
from django.test import TransactionTestCase
from orders.models import Order


class OrderAlertTest(TransactionTestCase):
    def test_send_sms_when_order_created(self):
        customer = Customer.objects.create(
            name="Jane", code="CUST.1234", mobile_number="+2549991112"
        )
        order = Order(customer=customer, item="Bike", amount=50000.00)

        with patch("orders.signals.send_sms") as mock_send_sms:
            order.save()

        mock_send_sms.assert_called_once_with(
            phone_number="+2549991112",
            message="Dear Jane, your order for Bike has been placed successfully!",
        )

    def test_dont_send_sms_when_order_updated(self):
        customer = Customer.objects.create(
            name="Jane", code="CUST.1234", mobile_number="+2549991112"
        )
        order = Order.objects.create(customer=customer, item="Bike", amount=50000.00)
        order.item = "Laptop"

        with patch("orders.signals.send_sms") as mock_send_sms:
            order.save()

        mock_send_sms.assert_not_called()
