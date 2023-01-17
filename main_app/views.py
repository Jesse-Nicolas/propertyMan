from django.shortcuts import render
from rest_framework import viewsets
from .models import Message, Manager, Client, Task, Action
from .serializers import MessageSerializer, ManagerSerializer, ClientSerializer, TaskSerializer, ActionSerializer
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser, FormParser
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView



# Create your views here.

class GoogleLogin(SocialLoginView):
    authentication_classes = []
    adapter_class = GoogleOAuth2Adapter

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.order_by('-sent')
    serializer_class = MessageSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()

class ManagerViewSet(viewsets.ModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.order_by('-added')
    serializer_class = TaskSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()

class ActionViewSet(viewsets.ModelViewSet):
    queryset = Action.objects.order_by('-start_time')
    serializer_class = ActionSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()