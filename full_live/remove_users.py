"""
import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'full_live.settings')
django.setup()

from users.models import User  # Import your User model

def remove_all_users():
    User.objects.all().delete()
    print("All users have been removed successfully.")

if __name__ == "__main__":
    remove_all_users()

"""