from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse

from speaker.models import Speaker
from .models import Presentation, Category


class PresentationTestMixin(object):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            first_name='Bahattin', last_name='Cinic',
            email='bahattincinic@gmail.com')
        self.presentation = Presentation.objects.create(
            speaker=self.speaker,
            title='Test Presentation',
            link='http://google.com/',
            description='Test Test Test')
        self.category = Category.objects.create(name='Test')
        self.presentation.categories.add(self.category)
        self.client = Client()


class HomeViewTest(PresentationTestMixin, TestCase):

    def test_homepage(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, self.speaker.get_fullname())
        self.assertContains(response, self.presentation.title)
        self.assertEqual(response.status_code, 200)


class PresentationTest(PresentationTestMixin, TestCase):

    def test_presentation_detail(self):
        response = self.client.get(self.presentation.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.presentation.title)

    def test_presentation_invalid(self):
        response = self.client.get(reverse('presentation-detail', args=[111]))
        self.assertEqual(response.status_code, 404)

    def test_presentation_list(self):
        response = self.client.get(reverse('presentation-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.presentation.title)

    def test_method_not_allowed(self):
        response_list = self.client.post(reverse('presentation-list'))
        response_detail = self.client.post(
            self.presentation.get_absolute_url())
        response_category = self.client.post(self.category.get_absolute_url())
        self.assertEqual(response_list.status_code, 405)
        self.assertEqual(response_detail.status_code, 405)
        self.assertEqual(response_category.status_code, 405)

    def test_category_detail(self):
        response = self.client.get(self.category.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.category.name)
        self.assertContains(response, self.presentation.title)

    def test_category_invalid(self):
        response = self.client.get(reverse('category-detail', args=[111]))
        self.assertEqual(response.status_code, 404)
