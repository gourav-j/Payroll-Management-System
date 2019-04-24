from django.test import TestCase
from django.urls import reverse

class AuthorListViewTest(TestCase):
	def test_view_url_accessible_by_name(self):
		response = self.client.get(reverse('index'))
		self.assertEqual(response.status_code, 200)
		