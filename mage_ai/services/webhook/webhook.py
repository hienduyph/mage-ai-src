import requests
from mage_ai.services.webhook.config import WebhookConfig


def send_webhook_message(
    config: WebhookConfig,
    message: str,
    title: str = None,
) -> None:
    message = message.replace("\\n", "\n")
    body = {
        "text": message,
    }
    resp = requests.post(config.webhook_url, json=body)
    if resp.status_code != 200:
        print("telegram_alert_error", resp.status_code, resp.text)
