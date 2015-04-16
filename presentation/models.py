from django.db import models
from django.utils.encoding import smart_text, python_2_unicode_compatible
from django.core.urlresolvers import reverse


@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return smart_text(self.name)

    def get_absolute_url(self):
        return reverse('category-detail', args=[self.id])


@python_2_unicode_compatible
class Presentation(models.Model):
    title = models.CharField(max_length=255)
    speaker = models.ForeignKey('speaker.Speaker',
                                related_name='presentations')
    link = models.URLField()
    description = models.TextField()
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return smart_text(self.title)

    def get_absolute_url(self):
        return reverse('presentation-detail', args=[self.id])
