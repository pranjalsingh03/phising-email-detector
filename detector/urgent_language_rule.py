from .base_rule import BaseRule
from config.settings import Settings

class UrgentLanguageRule(BaseRule):
    def check(self, email: dict) -> bool:
        pass
