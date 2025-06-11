# scripts/seed_shows.py

import os
import django

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from itineraries.models import Show

# Optional: Clear existing shows if you want a clean slate
Show.objects.all().delete()

# Example shows
shows = [
    {
        "name": "Sir Laughalot's Medieval Comedy Hour",
        "venue": "Assembly Hall",
        "time": "19:30",
        "dates": ["2025-08-01", "2025-08-02", "2025-08-03"],
    },
    {
        "name": "Shakespeare on a Scooter",
        "venue": "Princes Street Gardens",
        "time": "14:00",
        "dates": ["2025-08-02", "2025-08-04", "2025-08-06"],
    },
    {
        "name": "Drunk History: The Live Experience",
        "venue": "The Stand Comedy Club",
        "time": "22:00",
        "dates": ["2025-08-01", "2025-08-02", "2025-08-03", "2025-08-04"],
    },
    {
        "name": "The World's Worst Magician",
        "venue": "Pleasance Courtyard",
        "time": "16:00",
        "dates": ["2025-08-01", "2025-08-02", "2025-08-03", "2025-08-04", "2025-08-05"],
    },
    {
        "name": "Jazz Hands and Dad Jokes",
        "venue": "The Hub",
        "time": "20:00",
        "dates": ["2025-08-01", "2025-08-02", "2025-08-03", "2025-08-04"],
    },
    {
        "name": "Strictly Come Fencing",
        "venue": "Gilded Balloon",
        "time": "21:00",
        "dates": ["2025-08-03", "2025-08-04", "2025-08-05"],
    },
    {
        "name": "Musical Theatre for People Who Hate Musicals",
        "venue": "Underbelly Cowgate",
        "time": "17:30",
        "dates": ["2025-08-01", "2025-08-03", "2025-08-05"],
    },
    {
        "name": "The Late Late Llama Show",
        "venue": "Voodoo Rooms",
        "time": "23:00",
        "dates": ["2025-08-01", "2025-08-02", "2025-08-04"],
    },
    {
        "name": "Science Experiments Gone Wrong (For Kids!)",
        "venue": "National Museum of Scotland",
        "time": "10:00",
        "dates": ["2025-08-01", "2025-08-02", "2025-08-03"],
    },
    {
        "name": "Interpretive Dance About Biscuits",
        "venue": "Dance Base",
        "time": "15:00",
        "dates": ["2025-08-02", "2025-08-04", "2025-08-06"],
    },
    {
        "name": "Competitive Speed Knitting",
        "venue": "Summerhall",
        "time": "13:00",
        "dates": ["2025-08-01", "2025-08-02", "2025-08-05"],
    },
    {
        "name": "Epic Fails of British History",
        "venue": "Scottish Storytelling Centre",
        "time": "18:00",
        "dates": ["2025-08-01", "2025-08-03", "2025-08-04"],
    },
    {
        "name": "Mime in the Dark",
        "venue": "Underbelly George Square",
        "time": "20:30",
        "dates": ["2025-08-02", "2025-08-03", "2025-08-05"],
    },
    {
        "name": "One Man and His Ukulele",
        "venue": "The Caves",
        "time": "19:00",
        "dates": ["2025-08-01", "2025-08-03", "2025-08-04"],
    },
    {
        "name": "The Invisible Magician",
        "venue": "The Giggle Factory",
        "time": "19:30",
        "dates": ["2025-08-01", "2025-08-02", "2025-08-03"],
    },
    {
        "name": "Dancing with Dinosaurs",
        "venue": "Banana Cabaret",
        "time": "20:30",
        "dates": ["2025-08-02", "2025-08-03", "2025-08-04"],
    },
    {
        "name": "Shakespeare for Dogs",
        "venue": "Laugh Lounge",
        "time": "21:30",
        "dates": ["2025-08-03", "2025-08-04", "2025-08-05"],
    },
    {
        "name": "Silent Opera",
        "venue": "The Chuckle Hut",
        "time": "19:30",
        "dates": ["2025-08-01", "2025-08-02", "2025-08-03"],
    },
    {
        "name": "The Human Jukebox",
        "venue": "Wacky Warehouse",
        "time": "20:30",
        "dates": ["2025-08-04", "2025-08-05", "2025-08-06"],
    },
    {
        "name": "Cooking with Clowns",
        "venue": "The Giggle Factory",
        "time": "21:30",
        "dates": ["2025-08-02", "2025-08-03", "2025-08-04"],
    },
    {
        "name": "Extreme Mime Show",
        "venue": "Banana Cabaret",
        "time": "19:30",
        "dates": ["2025-08-01", "2025-08-03", "2025-08-05"],
    },
    {
        "name": "Karaoke Shakespeare",
        "venue": "Laugh Lounge",
        "time": "20:30",
        "dates": ["2025-08-02", "2025-08-04", "2025-08-06"],
    },
    {
        "name": "Stand-up Physics",
        "venue": "The Chuckle Hut",
        "time": "21:30",
        "dates": ["2025-08-01", "2025-08-02", "2025-08-03"],
    },
    {
        "name": "The Ukulele Orchestra of Doom",
        "venue": "Wacky Warehouse",
        "time": "19:30",
        "dates": ["2025-08-02", "2025-08-04", "2025-08-06"],
    },
    {
        "name": "Disco Yoga",
        "venue": "The Giggle Factory",
        "time": "20:30",
        "dates": ["2025-08-01", "2025-08-03", "2025-08-05"],
    },
    {
        "name": "Haunted History Tour",
        "venue": "Banana Cabaret",
        "time": "21:30",
        "dates": ["2025-08-02", "2025-08-04", "2025-08-06"],
    },
    {
        "name": "Bingo with Puppets",
        "venue": "Laugh Lounge",
        "time": "19:30",
        "dates": ["2025-08-01", "2025-08-02", "2025-08-03"],
    },
    {
        "name": "Jazzercise through the Ages",
        "venue": "The Chuckle Hut",
        "time": "20:30",
        "dates": ["2025-08-02", "2025-08-04", "2025-08-06"],
    },
    {
        "name": "The Great Spaghetti Juggling",
        "venue": "Wacky Warehouse",
        "time": "21:30",
        "dates": ["2025-08-03", "2025-08-05", "2025-08-07"],
    },
]


# Seed the shows
for show_data in shows:
    Show.objects.create(**show_data)

print(f"✅ Seeded {len(shows)} shows successfully!")
