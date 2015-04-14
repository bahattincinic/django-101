from django.db import models
from django.utils.encoding import smart_text, python_2_unicode_compatible


@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return smart_text(self.name)


@python_2_unicode_compatible
class Presentation(models.Model):
    title = models.CharField(max_length=255)
    speaker = models.ForeignKey('speaker.Speaker')
    link = models.URLField()
    description = models.TextField()
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return smart_text(self.title)
