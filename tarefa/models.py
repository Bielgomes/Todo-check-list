from django.db import models

from user.models import Profile


class TaskStatus(models.TextChoices):
    TODO = 'TODO'
    DONE = 'DONE'


class Task(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=150, null=True)
    status = models.CharField(max_length=20, choices=TaskStatus.choices, default=TaskStatus.TODO)
    category = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(null=True, auto_now=True)

    user = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
