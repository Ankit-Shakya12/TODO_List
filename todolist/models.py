from django.db import models

# Create your models here.

class toDolist(models.Model):
    tasks = models.CharField(max_length=50)
    complete = models.BooleanField(default=False)
    create_at = models.DateTimeField()

    def __str__(self):
        return self.tasks

