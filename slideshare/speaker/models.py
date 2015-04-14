from django.db import models
from django.utils.encoding import smart_text, python_2_unicode_compatible


@python_2_unicode_compatible
class Speaker(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()

    def get_fullname(self):
        return '%s %s' % (self.first_name, self.last_name)

    def __str__(self):
        return smart_text(self.get_fullname())
