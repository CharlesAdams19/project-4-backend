
from django.contrib.auth import get_user_model

User = get_user_model()

def run():
    users = [
        {'username': 'user1', 'password': 'password123'},
        {'username': 'user2', 'password': 'password123'},
        {'username': 'user3', 'password': 'password123'},
    ]

    for user_data in users:
        if not User.objects.filter(username=user_data['username']).exists():
            user = User.objects.create_user(
                username=user_data['username'],
                password=user_data['password']
            )
            print(f'✅ Created user: {user.username}')
        else:
            print(f'⚠️ User already exists: {user_data["username"]}')

    print('User seeding complete!')
