from django.test import TestCase
from django.contrib.messages import get_messages


class TestViews(TestCase):

    def test_GET_home_page(self):
        url = self.client.get('/')
        self.assertEqual(url.status_code, 200)
        self.assertTemplateUsed(url, 'index.html')

    def test_GET_about_page(self):
        url = self.client.get('/about/')
        self.assertEqual(url.status_code, 200)
        self.assertTemplateUsed(url, 'about.html')

    def test_GET_contact_page(self):
        url = self.client.get('/contact/')
        self.assertEqual(url.status_code, 200)
        self.assertTemplateUsed(url, 'contact.html')

    def test_GET_menu_page(self):
        url = self.client.get('/menu/')
        self.assertEqual(url.status_code, 200)
        self.assertTemplateUsed(url, 'menu.html')

    def test_Get_reservations_page(self):
        url = self.client.get('/reservations/')
        self.assertEqual(url.status_code, 200)
        self.assertTemplateUsed(url, 'reservations.html')
