import logging

import requests
from django.conf import settings

logger = logging.getLogger(__name__)
LOG_PREFIX = "[africastalking]"


def send_sms(phone_number: str, message: str) -> None:
    """Deliver an SMS via the AfricasTalking API.

    Args:
      phone_number: The recipient's mobile number.
      message: The message string.
    """
    headers = {
        "Apikey": settings.AFRICAS_TALKING_API_KEY,
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = {
        "username": settings.AFRICAS_TALKING_USERNAME,
        "to": phone_number,
        "message": message,
    }
    try:
        response = requests.post(
            f"{settings.AFRICAS_TALKING_BASE_URL}/messaging",
            headers=headers,
            data=data,
        )
        logger.info(f"{LOG_PREFIX} received reponse: {response.json()}")
    except requests.exceptions.RequestException as e:
        logger.warning(f"{LOG_PREFIX} failed to send SMS to {phone_number}:\n{e}")
