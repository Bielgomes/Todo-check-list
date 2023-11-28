from rest_framework.serializers import ModelSerializer

from task.models import Task


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'name', 'description', 'status', 'category',
                  'created_at', 'edited_at', 'user')
        read_only_fields = ('status', 'created_at', 'edited_at', 'user')