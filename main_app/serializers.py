from rest_framework import serializers
from .models import Todo

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('author', 'recipient', 'sent', 'text', 'image_url')

class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('name', 'phone', 'bio')

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('name', 'address', 'phone', 'p_manager')

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('client', 'details', 'image_url', 'completed')

class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('task', 'start_time', 'details', 'image_url', 'time_spent')
