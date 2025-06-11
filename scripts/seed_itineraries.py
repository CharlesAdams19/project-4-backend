# scripts/seed_itineraries.py

import random
from django.contrib.auth import get_user_model
from itineraries.models import Itinerary, Show
from django.utils.timezone import now, timedelta

User = get_user_model()

def run():
    Itinerary.objects.all().delete()

    users = User.objects.all()
    shows = list(Show.objects.all())

    for user in users:
        num_itins = random.randint(1, 2)

        for i in range(num_itins):
            itin_name = f"{user.username}'s Itinerary {i+1}"

            itinerary_items = []
            selected_shows = random.sample(shows, k=random.randint(2, 5))

            for show in selected_shows:
                # Pick a random date
                date = random.choice(show.dates)
                start_time = f"{show.time}:00"
                start_dt = f"{date}T{show.time}:00"
                end_dt = f"{date}T{int(show.time.split(':')[0]) + 1}:30:00"

                itinerary_items.append({
                    'id': random.randint(1000, 9999),  # unique random id
                    'show_name': show.name,
                    'start': start_dt,
                    'end': end_dt,
                    'venue': show.venue
                })

            Itinerary.objects.create(
                name=itin_name,
                user=user,
                itinerary_items=itinerary_items
            )

            print(f'✅ Created itinerary: {itin_name} for {user.username}')

    print('✅ Itinerary seeding complete!')
