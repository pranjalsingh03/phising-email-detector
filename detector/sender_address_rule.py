from .base_rule import BaseRule
from config.settings import Settings

class SenderAddressRule(BaseRule):
    def check(self, email: dict) -> bool:
        pass