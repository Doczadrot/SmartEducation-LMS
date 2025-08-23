import re
from rest_framework.exceptions import ValidationError

class LinkValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):

        if not re.search('youtube.com', value):
            raise ValidationError('Недоступный формат ссылки')