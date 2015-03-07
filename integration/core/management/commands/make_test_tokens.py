from django.core.management.base import BaseCommand

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):

        try:
            admin = User.objects.get(username="admin")
        except User.DoesNotExist:
            admin = User.objects.create_superuser(
                username="admin",
                email="tech@theonion.com",
                password="testing")

        Token.objects.get_or_create(user=admin, key="notarealkey")
