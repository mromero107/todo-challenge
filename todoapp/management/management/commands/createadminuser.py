from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Create an admin superuser'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='Enter the username of the superuser')
        parser.add_argument('email', type=str, help='Enter the email of the superuser')
        parser.add_argument('password', type=str, help='Enter the password of the superuser')

    def handle(self, *args, **options):
        User = get_user_model()
        username = options['username']
        email = options['email']
        password = options['password']

        if User.objects.filter(username=username).exists():
            raise CommandError('User "%s" already exists' % username)

        User.objects.create_superuser(username=username, email=email, password=password)
        self.stdout.write(self.style.SUCCESS('Successfully created superuser "%s"' % username))
