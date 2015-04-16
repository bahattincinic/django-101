from django.test import TestCase
from django.core.urlresolvers import reverse

from presentation.tests import PresentationTestMixin


class SpeakerTest(PresentationTestMixin, TestCase):

    def test_speaker_list(self):
        response = self.client.get(reverse('speaker-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.speaker.get_fullname())

    def test_speaker_detail(self):
        response = self.client.get(self.speaker.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.speaker.get_fullname())

    def test_speaker_invalid(self):
        response = self.client.get(reverse('speaker-detail', args=[111]))
        self.assertEqual(response.status_code, 404)

    def test_method_not_allowed(self):
        response_list = self.client.post(reverse('speaker-list'))
        response_detail = self.client.post(
            self.speaker.get_absolute_url())
        self.assertEqual(response_list.status_code, 405)
        self.assertEqual(response_detail.status_code, 405)
