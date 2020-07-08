from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from users.models import Users, ActivityPeriod
from datetime import datetime, timedelta
import pytz
import random
import string


class Command(BaseCommand):
    help = 'Create random users'

    def add_arguments(self, parser):
        parser.add_argument('--users', type=int,
                            help='Indicates the number of users to be created')
        parser.add_argument('--activities', type=int,
                            help='Indicates the number of activities to be created per user')

    def handle(self, *args, **kwargs):
        users = kwargs['users']
        activities = kwargs['activities']
        for user in range(users):
            user_id = ''.join(random.choices(
                string.ascii_letters + string.digits, k=10))
            created_user = Users.objects.create(id=user_id,
                                                FirstName=get_random_string(), LastName=get_random_string())
            self.stdout.write("User created")
            self.stdout.write(user_id)
            for activity in range(activities):
                created_user_activity = ActivityPeriod.objects.create(
                    User=created_user,
                    StartTime=datetime.now(pytz.timezone(
                        created_user.Timezone)) - timedelta(minutes=random.randint(0, 20)),
                    EndTime=datetime.now(pytz.timezone(
                        created_user.Timezone)) + timedelta(minutes=random.randint(0, 20))
                )
