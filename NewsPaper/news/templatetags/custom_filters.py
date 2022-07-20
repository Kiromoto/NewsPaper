from django import template
from flashtext import KeywordProcessor

OBSCENE_WORDS = {}

register = template.library()
keyword_processor = KeywordProcessor()


@register.filter()
def makegoodwords(value):
    return value

