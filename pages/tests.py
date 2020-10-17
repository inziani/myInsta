from django.test import TestCase, SimpleTestCase
from django.contrib.auth import get_user_model
django.urls import reverse

class HomaPageTests(SimpleTestCase):

  def test_home_page_status(self):
    response = self.client.get('/')
    self.assertEqual(response.status_code, 200)

  def test_view_url_name(self):
    response = self.client.get(reverse('home'))
    self.assertEqual(response.status_code, 200)


