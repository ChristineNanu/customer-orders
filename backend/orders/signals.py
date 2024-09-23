from django.db.models.signals import post_save
from django.dispatch import receiver
from integrations.africas_talking import send_sms
from orders.models import Order

CUSTOMER_ORDER_CONFIRMATION_MESSAGE = (
    "Dear {name}, your order for {item} has been placed successfully!"
)


@receiver(post_save, sender=Order)
def notify_customer_order_placed(sender, instance, created: bool, **kwargs) -> None:
    """Inform the customer that an order has been placed."""
    if not created:
        return

    message = CUSTOMER_ORDER_CONFIRMATION_MESSAGE.format(
        name=instance.customer.name,
        item=instance.item,
    )
    send_sms(
        phone_number=instance.customer.mobile_number,
        message=message,
    )
