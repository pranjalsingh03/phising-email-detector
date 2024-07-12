from .base_rule import BaseRule
from config.settings import Settings

class UrgentLanguageRule(BaseRule):
    def check(self, email: dict) -> bool:
        settings = Settings()
        urgent_keywords = settings.get_setting('urgent_keywords')
        subject_and_body = email['subject'] + ' ' + email['body']
        return any(keyword in subject_and_body.lower() for keyword in urgent_keywords)
