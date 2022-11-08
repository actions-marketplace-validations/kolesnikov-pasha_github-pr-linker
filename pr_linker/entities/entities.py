from enum import Enum


class EventAction(Enum):
    OPENED = "opened"
    EDITED = "edited"
    CLOSED = "closed"
    REOPENED = "reopened"
    SYNCRONIZE = "synchronize"
    CONVERTED_TO_DRAFT = "converted_to_draft"
    READY_FOR_REVIEW = "ready_for_review"
    REVIEW_REQUESTED = "review_requested"
    MERGED = "merged"


class Text:
    def __init__(self, text, is_bold=False, href=None):
        self.text = text
        self.is_bold = is_bold
        self.href = href


    def __eq__(self, __o: object) -> bool:
        return __o.text == self.text \
            and __o.is_bold == self.is_bold \
            and __o.href == self.href


    def __str__(self) -> str:
        return self.text