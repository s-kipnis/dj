from django.urls import resolve
from django.test import TestCase
from lists.views import home_page
from django.http import HttpRequest

class HomePageTest(TestCase):
    """тест домашней страницы"""
    def test_root_url_resolves_to_home_page_view(self):
        """тест: корневой url преобразуется в представление 
           домашней страницы"""
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_uses_home_template(self):
        """тест: используется домашний шаблон"""
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')