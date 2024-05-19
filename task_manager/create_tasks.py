import os
import django
from faker import Faker

# Set up the Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_manager.settings')
django.setup()

from tasks.models import Task, User
from django.utils import timezone

fake = Faker()

# Assuming you have at least one user in your database
user = User.objects.first()
if not user:
    print("No users found in the database. Please create a user first.")
    exit()

tasks = []
for _ in range(200):
    task = Task(
        title=fake.sentence(nb_words=6),
        description=fake.text(max_nb_chars=200),
        done=fake.boolean(),
        user=user,
        created_at=timezone.now(),
        updated_at=timezone.now()
    )
    tasks.append(task)

Task.objects.bulk_create(tasks)
print("200 tasks created successfully!")
