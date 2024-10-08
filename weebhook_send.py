import os
import requests


class WebhookSend:
    @staticmethod
    def send_message(message: str):
        """
        Sends a message to a specified webhook URL.

        Args:
        - message (str): The message to be sent to the webhook.

        Returns:
        - None
        """
        webhook_url = os.getenv("WEBHOOK_URL")
        data = {
            "content": message
        }
        requests.post(webhook_url, json=data)
