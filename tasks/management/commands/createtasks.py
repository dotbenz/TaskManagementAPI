from django.core.management.base import BaseCommand
from tasks.models import Task, User
from django.utils import timezone

class Command(BaseCommand):
    help = 'Create 200 sample tasks'

    def handle(self, *args, **kwargs):
        user = User.objects.first()
        if not user:
            self.stdout.write(self.style.ERROR('No users found in the database. Please create a user first.'))
            return

        tasks = []
        for i in range(200):
            task = Task(
                title=f'Task {i+1}',
                description=f'Description for task {i+1}',
                done=False,
                user=user,
                created_at=timezone.now(),
                updated_at=timezone.now()
            )
            tasks.append(task)

        Task.objects.bulk_create(tasks)
        self.stdout.write(self.style.SUCCESS('200 tasks created successfully!'))
