from django.db import models


class Book(models.Model):
    title = models.CharField(250)
    subtitle = models.CharField(250)
    author = models.CharField(100)
    isbn = models.CharField(10)

    def __str__(self):
        return self.title
