from django.db import models
from django.contrib.auth.models import User

def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

# Create your models here.

class Message(models.Model):
  author = models.ForeignKey(User, related_name='%(app_label)sauthor%(class)s', on_delete=models.CASCADE)
  recipient = models.ForeignKey(User, on_delete=models.CASCADE)
  sent = models.DateTimeField(auto_now_add=True)
  text = models.TextField()
  image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)

class Manager(User):
  name = models.CharField(max_length=50)
  phone = models.CharField(max_length=10)
  bio = models.TextField()

class Client(User):
  name = models.CharField(max_length=50)
  address = models.CharField(max_length=100)
  phone = models.CharField(max_length=10)
  p_manager = models.ForeignKey(Manager, on_delete=models.CASCADE)

class Task(models.Model):
  client = models.ForeignKey(Client, on_delete=models.CASCADE)
  details = models.TextField()
  image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)
  completed = models.BooleanField()

class Action(models.Model):
  task = models.ForeignKey(Task, on_delete=models.CASCADE)
  start_time = models.DateTimeField(auto_now_add=True)
  details = models.TextField()
  image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)   #finish setup for image upload! article online ;)
  time_spent = models.DurationField()

