from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_done = models.BooleanField(default=False)
    
    class Meta:
        db_table = "todo"
        verbose_name = "todo"
        verbose_name_plural = "todos"
        ordering = ["-id"]

    def __str__(self):
        return self.name
