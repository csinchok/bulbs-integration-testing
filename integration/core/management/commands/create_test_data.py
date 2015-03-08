import datetime
from django.core.management.base import BaseCommand

from django.contrib.auth.models import User, Group
from django.db import transaction
from django.utils import timezone
from rest_framework.authtoken.models import Token

from bulbs.content.models import Content, FeatureType, Tag

from integration.core.models import Article

import itertools

FEATURE_TYPES = [
    "Blog",
    "Thinkpiece",
    "Reflection",
    "Clickbait"
]

TAGS = [
    "OMG",
    "WOW",
    "Inspiring",
    "Silly"
]

AUTHORS = [
    {
        "first_name": "Milque",
        "last_name": "Toast",
        "username": "mtoast",
        "email": "mtoast@theonion.com"
    },
    {
        "first_name": "Bobby",
        "last_name": "Nutson",
        "username": "bnutson",
        "email": "bnutson@theonion.com"
    },
    {
        "first_name": "Homer",
        "last_name": "Simpson",
        "username": "hsimpson",
        "email": "hsimpson@theonion.com"
    },
    {
        "first_name": "Spanky",
        "last_name": "McDougal",
        "username": "smcdougal",
        "email": "smcdougal@theonion.com"
    },
    {
        "first_name": "Chuckles",
        "last_name": "Cunningham",
        "username": "ccunningham",
        "email": "ccunningham@theonion.com"
    }
]


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):

        author_group = Group.objects.get(name="author")
        
        with transaction.atomic():
            try:
                admin = User.objects.get(username="admin")
            except User.DoesNotExist:
                admin = User.objects.create_superuser(
                    username="admin",
                    email="tech@theonion.com",
                    password="testing")

            authors = []
            for data in AUTHORS:
                try:
                    author = User.objects.get(username=data["username"])
                except User.DoesNotExist:
                    author = User.objects.create_user(password="noop", **data)
                author.groups.add(author_group)
                authors.append(author)

            feature_types = []
            for name in FEATURE_TYPES:
                ft, created = FeatureType.objects.get_or_create(name=name)
                feature_types.append(ft)

            tags = []
            for name in TAGS:
                tag, created = Tag.objects.get_or_create(name=name)
                tags.append(tag)

        with transaction.atomic():
            for ft in feature_types:
                counter = 0
                for tag_com in itertools.combinations_with_replacement(tags, 2):
                    for author_com in itertools.combinations_with_replacement(authors, 3):
                        article, created = Article.objects.get_or_create(
                            title="{}: {}".format(ft.name, counter),
                            feature_type=ft,
                            defaults={
                                'published': timezone.now() - datetime.timedelta(hours=1)
                            }
                        )
                        for tag in tag_com:
                            article.tags.add(tag)

                        for author in author_com:
                            article.authors.add(author)

                        counter += 1

        Token.objects.get_or_create(user=admin, key="notarealkey")
