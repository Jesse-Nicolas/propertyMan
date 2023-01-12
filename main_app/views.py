from django.shortcuts import render
from rest_framework import viewsets

from .models import Message, Task, Action
from .serializers import MessageSerializer, TaskSerializer, ActionSerializer
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser, FormParser


# Create your views here.
class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.order_by('-creation_date')
    serializer_class = MessageSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.order_by('-creation_date')
    serializer_class = TaskSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

class ActionViewSet(viewsets.ModelViewSet):
    queryset = Action.objects.order_by('-creation_date')
    serializer_class = ActionSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)