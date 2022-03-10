import random
from datetime import datetime
from django.core.management.base import BaseCommand
from django_seed import Seed
from users.models import User
from rooms.models import Room, Photo
from reviews.models import Review


class Command(BaseCommand):

    help = "It seeds the DB with tons of stuff"

    def handle(self, *args, **options):
        # user_seeder = Seed.seeder()
        # user_seeder.add_entity(User, 20, {"is_staff": False, "is_superuser": False})
        # user_seeder.execute()

        users = User.objects.all()
        # room_seeder = Seed.seeder()
        # room_seeder.add_entity(
        #     Room,
        #     150,
        #     {
        #         "host": lambda x: random.choice(users),
        #         "name": lambda x: room_seeder.faker.street_address(),
        #         "price": lambda x: random.randint(0, 300),
        #         "beds": lambda x: random.randint(0, 5),
        #         "guests": lambda x: random.randint(1, 6),
        #         "bedrooms": lambda x: random.randint(0, 3),
        #         "bathrooms": lambda x: random.randint(0, 5),
        #         "instant_book": lambda x: random.choice([True, False]),
        #         "check_in": lambda x: datetime.now(),
        #         "check_out": lambda x: datetime.now(),
        #     },
        # )
        # room_seeder.execute()

        rooms = Room.objects.all()
        # # Photos
        # for room in rooms:
        #     for i in range(random.randint(5, 10)):
        #         Photo.objects.create(
        #             caption=room_seeder.faker.sentence(),
        #             room=room,
        #             file=f"room_photos/{random.randint(1, 31)}.webp",
        #         )

        review_seeder = Seed.seeder()
        review_seeder.add_entity(Review, 150, {
            "review": lambda x: review_seeder.faker.paragraph(nb_sentences=1),
            "accuracy": lambda x: random.randint(1, 5),
            "communication": lambda x: random.randint(1, 5),
            "cleanliness": lambda x: random.randint(1, 5),
            "location": lambda x: random.randint(1, 5),
            "check_in": lambda x: random.randint(1, 5),
            "value": lambda x: random.randint(1, 5),
            "user": lambda x:  random.choice(users),
            "room": lambda x:  random.choice(rooms),
        })

        review_seeder.execute()

        self.stdout.write(self.style.SUCCESS(f"Everything seeded"))
