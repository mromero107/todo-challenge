import uuid
from django.db import models

class Task(models.Model):
    """
    Represents a task in the todo app.

    Attributes:
        id (UUIDField): The unique identifier for the task.
        title (CharField): The title of the task.
        is_done (BooleanField): Indicates whether the task is done or not.
        created_at (DateTimeField): The date and time when the task was created.
        updated_at (DateTimeField): The date and time when the task was last updated.
    """

    id = models.UUIDField(default=uuid.uuid4, unique=True,
        primary_key=True, editable=False)
    title = models.CharField(max_length=255)
    is_done = models.BooleanField(default=False, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    