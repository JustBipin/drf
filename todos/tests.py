from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Todo
from rest_framework import response


class TodoModelTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.todo1 = Todo.objects.create(title="First Todo", body="A body of text here")
        cls.todo2 = Todo.objects.create(title="Second Todo", body="A body of text here")

    def test_model_content(self):
        self.assertEqual(self.todo1.title, "First Todo")
        self.assertEqual(self.todo1.body, "A body of text here")
        self.assertEqual(str(self.todo1), "First Todo")

    def test_api_list_view(self):
        response = self.client.get("/api/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.todo1)
        self.assertContains(response, self.todo2)

    def test_api_detail_view(self):
        response = self.client.get(f"/api/{self.todo1.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.todo1)
