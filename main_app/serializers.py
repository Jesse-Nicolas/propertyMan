from rest_framework import serializers
from .models import Message, Manager, Client, Task, Action

class MessageSerializer(serializers.ModelSerializer):
    image_url = serializers.ImageField(required=False)
    class Meta:
        model = Message
        fields = ('author', 'recipient', 'sent', 'text', 'image_url')

class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = ('phone', 'bio')

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('address', 'phone', 'p_manager')

class TaskSerializer(serializers.ModelSerializer):
    image_url = serializers.ImageField(required=False)
    class Meta:
        model = Task
        fields = ('client', 'details', 'image_url', 'completed')

class ActionSerializer(serializers.ModelSerializer):
    image_url = serializers.ImageField(required=False)
    class Meta:
        model = Action
        fields = ('task', 'start_time', 'details', 'image_url', 'time_spent')
