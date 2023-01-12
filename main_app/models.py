from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Message(models.Model):
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  recipient = models.ForeignKey(User, on_delete=models.CASCADE)
  sent = models.DateTimeField(auto_now_add=True)
  text = models.TextField()
  image = models.ImageField()

class Manager(User):
  name = models.CharField(max_length=50)
  phone = models.CharField(max_length=10)
  bio = models.TextField()

class Client(User):
  name = models.CharField(max_length=50)
  address = models.CharField(max_length=100)
  phone = models.CharField(max_length=10)
  manager = models.ForeignKey(Manager, on_delete=models.CASCADE)

class Task(models.Model):
  client = models.ForeignKey(Client, on_delete=models.CASCADE)
  details = models.TextField()
  image = models.ImageField()
  completed = models.BooleanField()

class Action(models.Model):
  task = models.ForeignKey(Task, on_delete=models.CASCADE)
  start_time = models.DateTimeField(auto_now_add=True)
  details = models.TextField()
  image = models.ImageField()   #finish setup for image upload! article online ;)
  time_spent = models.DurationField()

