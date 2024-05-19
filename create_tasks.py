# populate_tasks.py

import os
import django
from django.utils import timezone
from faker import Faker
from tasks.models import Task
from django.contrib.auth import get_user_model

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_manager.settings')
django.setup()

def create_tasks(num_tasks):
    fake = Faker()
    User = get_user_model()

    # Create tasks
    for _ in range(num_tasks):
        user = User.objects.order_by('?').first()
        title = fake.sentence()
        description = fake.paragraph()
        done = fake.boolean()
        created_at = timezone.now()
        updated_at = created_at

        Task.objects.create(user=user, title=title, description=description, done=done, created_at=created_at, updated_at=updated_at)

def main():
    num_tasks = 200
    create_tasks(num_tasks)
    print(f"{num_tasks} tasks created successfully.")

if __name__ == '__main__':
    main()
