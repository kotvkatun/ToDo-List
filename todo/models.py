from django.db import models
from userauth.models import User

# Create your models here.
class ToDoLists(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, name="owner")
    todolist = models.JSONField(name="todolist", default=dict)
    
    def __str__(self):
        return f"Todo list of {self.owner}"
    