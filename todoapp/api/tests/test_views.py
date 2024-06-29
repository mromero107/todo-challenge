import pytest
from django.utils import timezone
from django.test import RequestFactory
from api.models import Task
from api.serializers import TaskSerializer
from api.views import TaskViewSet

@pytest.mark.django_db
def test_task_viewset_create():
    task_data = {
        "title": "Sample Task",
        "is_done": False,
        "created_at": timezone.now(),
        "updated_at": timezone.now()
    }
    serializer = TaskSerializer(data=task_data)
    assert serializer.is_valid()
    task = serializer.save()
    assert task.title == "Sample Task"
    assert task.is_done == False
    assert task.created_at <= timezone.now()
    assert task.updated_at <= timezone.now()

@pytest.mark.django_db
def test_task_viewset_update():
    task = Task.objects.create(title="Sample Task", is_done=False)
    task_data = {
        "title": "Updated Task",
        "is_done": True,
        "created_at": task.created_at,
        "updated_at": timezone.now()
    }
    serializer = TaskSerializer(instance=task, data=task_data)
    assert serializer.is_valid()
    updated_task = serializer.save()
    assert updated_task.title == "Updated Task"
    assert updated_task.is_done == True
    assert updated_task.updated_at >= task.updated_at

@pytest.mark.django_db
def test_task_viewset_delete():
    task = Task.objects.create(title="Sample Task", is_done=False)
    task_id = task.id
    viewset = TaskViewSet()
    viewset.kwargs = {"pk": task_id}
    request = RequestFactory().delete("/dummy-url/")
    viewset.request = request
    viewset.destroy(request, pk=task_id)
    with pytest.raises(Task.DoesNotExist):
        Task.objects.get(id=task_id)
