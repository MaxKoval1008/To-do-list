from django.db import models


class Task(models.Model):
    task_name = models.CharField(max_length=100)
    task_description = models.TextField(max_length=1000, null=True, blank=True)
    task_time = models.TimeField()
    complete_choice = models.BooleanField(default=None)

    def __str__(self):
        return self.task_name
