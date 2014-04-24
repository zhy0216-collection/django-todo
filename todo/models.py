import datetime
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone 

# Create your models here.
class TodoList(models.Model):
    name        = models.TextField()
    author      = models.ForeignKey(User)
    create_time = models.DateTimeField(auto_now_add=True)


    def __unicode__(self):
        return self.name


class TodoItem(models.Model):
    content     = models.TextField()
    todo_list   = models.ForeignKey(TodoList)

    def __unicode__(self):
        return self.content


