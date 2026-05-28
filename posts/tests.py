from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Post
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework.status import *


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # test user
        cls.user = get_user_model().objects.create_user(
            username="testuser",
            email="test@email.com",
            password="secret",
        )

        # test post
        cls.post_1 = Post.objects.create(
            author=cls.user,
            title="A good title",
            body="Nice body content",
        )
        cls.post_2 = Post.objects.create(
            author=cls.user,
            title="short title",
            body="this is\na multiline\nbody",
        )

    def test_post_model(self):
        self.assertEqual(str(self.post_1), "A good title")
        self.assertEqual(self.post_1.author.username, "testuser")
        self.assertEqual(self.post_1.title, "A good title")
        self.assertEqual(self.post_1.body, "Nice body content")

    def test_post_api(self):
        user = get_user_model().objects.get(username="testuser")
        client = APIClient()
        client.force_authenticate(user=user)
        response = client.get("/api/v1/1/")
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertContains(response, "A good title")
        self.assertContains(response, self.user.id)

    def test_post_api(self):
        user = get_user_model().objects.get(username="testuser")
        client = APIClient()
        client.force_authenticate(user=user)
        response = client.get("/api/v1/")
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertContains(response, "A good title")
        self.assertContains(response, "short title")
        self.assertContains(response, self.user.id)
