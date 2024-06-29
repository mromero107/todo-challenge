import pytest
from django.utils import timezone
from api.models import Task

@pytest.mark.django_db
def test_task_creation():
    task = Task.objects.create(title="Sample Task")
    assert task.title == "Sample Task"
    assert task.is_done == False
    assert task.created_at <= timezone.now()
    assert task.updated_at <= timezone.now()

@pytest.mark.django_db
def test_task_update():
    task = Task.objects.create(title="Sample Task")
    task.title = "Updated Task"
    task.is_done = True
    task.save()
    updated_task = Task.objects.get(id=task.id)
    assert updated_task.title == "Updated Task"
    assert updated_task.is_done == True
    assert updated_task.updated_at >= task.updated_at

@pytest.mark.django_db
def test_task_deletion():
    task = Task.objects.create(title="Sample Task")
    task_id = task.id
    task.delete()
    with pytest.raises(Task.DoesNotExist):
        Task.objects.get(id=task_id)