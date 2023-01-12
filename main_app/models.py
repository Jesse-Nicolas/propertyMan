from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
  user = models.ForeignKey(
    User,
    #unique setting for one-to-one relationship
    unique=True,
    on_delete=models.CASCADE,
  )
  name = models.CharField(max_length=50)
  address = models.CharField(max_length=100)
  is_manager = models.BooleanField()
  tasks = models.ManyToOneRel()


class Task(models.Model):
  name = models.CharField(max_length=200)
  client = models.ForeignKey(
    User, 
    #one-to-many
    on_delete=models.CASCADE,
  )
  