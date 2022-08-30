from django.test import TestCase, SimpleTestCase

# Create your tests here.

class SimpleTests(SimpleTestCase):
	"""docstring for SimpleTests"""

	#test for homepage 
	def test_home_page_status_code(self):
		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)

	#test for about page
	def test_about_page_status_code(self):
		response =self.client.get('/about/')
		self.assertEqual(response.status_code, 200)
		