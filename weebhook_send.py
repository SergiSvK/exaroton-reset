import os
import requests


class WebhookSend:
    @staticmethod
    def send_message(message: str):
        webhook_url = os.getenv("WEBHOOK_URL")
        data = {
            "content": message
        }
        requests.post(webhook_url, json=data)

