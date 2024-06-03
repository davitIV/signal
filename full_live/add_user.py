# users/add_user.py
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'full_live.settings')
django.setup()

def add_user():
    from users.models import User

    name = input("Enter name: ")
    email = input("Enter email: ")

    user = User.objects.create(name=name, email=email)
    print(f"User {name} added successfully with email {email}.")

if __name__ == "__main__":
    add_user()
