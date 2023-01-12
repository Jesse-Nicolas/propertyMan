from django.contrib import admin
from .models import Message, Manager, Client, Task, Action

# Register your models here.

class MessageAdmin(admin.ModelAdmin):
  list_display = ('author', 'recipient', 'sent', 'text', 'image_url')

class ManagerAdmin(admin.ModelAdmin):
  list_display = ('name', 'phone', 'bio')

class ClientAdmin(admin.ModelAdmin):
  list_display = ('name', 'address', 'phone', 'p_manager')

class TaskAdmin(admin.ModelAdmin):
  list_display = ('client', 'details', 'image_url', 'completed')

class ActionAdmin(admin.ModelAdmin):
  list_display = ('task', 'start_time', 'details', 'image_url', 'time_spent')


admin.site.register(Message, MessageAdmin, Manager, ManagerAdmin, Client, ClientAdmin, Task, TaskAdmin, Action, ActionAdmin)