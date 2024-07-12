from .base_rule import BaseRule
from config.settings import Settings

class SenderAddressRule(BaseRule):
    def check(self, email: dict) -> bool:
        settings = Settings()
        suspicious_domains = settings.get_setting('suspicious_domains')
        return any(domain in email['from'] for domain in suspicious_domains)
