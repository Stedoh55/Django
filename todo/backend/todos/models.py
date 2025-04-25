from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    create_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title