import math

from django.utils import timezone
from rest_framework import permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from tarefa.api.serializers import TasksSerializer
from tarefa.models import Task


class TasksViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TasksSerializer

    permission_classes = (permissions.IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        new_task = Task.objects.create(**request.data, user=request.user)
        serializer = TasksSerializer(new_task)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        category = request.query_params.get('category', '')
        tasks = self.queryset.filter(user=request.user, category__contains=category)
        if not tasks:
            return Response({})

        page = int(request.query_params.get('page', 1))
        page_size = int(request.query_params.get('page_size', 25))

        task_count = tasks.count()
        total_pages = math.ceil(task_count / page_size)

        start_index = (int(page) - 1) * int(page_size)
        end_index = start_index + int(page_size)

        tasks = tasks[start_index:end_index]

        serializer = TasksSerializer(tasks, many=True)

        response = {
            'page': page,
            'page_size': page_size,
            'page_count': total_pages,
            'results': serializer.data
        }

        return Response(response)

    def retrieve(self, request, *args, **kwargs):
        try:
            task = self.queryset.get(id=kwargs['pk'], user=request.user)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = TasksSerializer(task)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        try:
            task = self.queryset.get(id=kwargs['pk'], user=request.user)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        try:
            task = self.queryset.get(id=kwargs['pk'], user=request.user)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        try:
            task = self.queryset.get(id=kwargs['pk'], user=request.user)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        task.delete()
        return Response(status=status.HTTP_200_OK)

    @action(methods=['POST'], detail=True)
    def check(self, request, pk=None):
        try:
            task = self.queryset.get(id=pk, user=request.user)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        task.status = "TODO" if task.status == "DONE" else "DONE"
        task.save()

        return Response(status=status.HTTP_202_ACCEPTED)
