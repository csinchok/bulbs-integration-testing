from django.db import models

from bulbs.content.models import Content


class Article(Content):
    body = models.TextField()
