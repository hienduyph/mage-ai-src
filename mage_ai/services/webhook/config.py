from dataclasses import dataclass
from mage_ai.shared.config import BaseConfig


@dataclass
class WebhookConfig(BaseConfig):
    webhook_url: str = None

    @property
    def is_valid(self) -> bool:
        hook = self.webhook_url is not None and self.webhook_url != "None"
        return hook
