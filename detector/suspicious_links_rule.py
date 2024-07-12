import re
from .base_rule import BaseRule
from config.settings import Settings

class SuspiciousLinksRule(BaseRule):
    def check(self, email: dict) -> bool:
        pass
