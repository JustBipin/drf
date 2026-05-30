from django.test import Client, SimpleTestCase
from django.urls import resolve, reverse

from .views import HomePageView


class HomePageTests(SimpleTestCase):
    @classmethod
    def setUpClass(cls):
        cls.response = Client().get("/")

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_url_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, "home.html")

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, "Homepage")

    def test_homepage_does_not_contain_incorrect_html(self):  # new
        self.assertNotContains(self.response, "the model shouldn't contain this text")

    def test_homepage_url_resolves_homepageview(self):
        view = resolve("/")
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)
