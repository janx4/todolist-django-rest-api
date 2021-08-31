from django.http.response import JsonResponse
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import TaskSerializers
from .models import Task



# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    return Response('Hello Guys')

@api_view(['GET'])
def task_list(request):
    tasks = Task.objects.all()
    serializer = TaskSerializers(tasks, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def task_detail(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializers(task, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def task_create(request):
    serializer = TaskSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def task_update(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializers(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def task_delete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response("Delete successfully!")