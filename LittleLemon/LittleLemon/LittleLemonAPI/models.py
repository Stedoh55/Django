from django.db import models
from datetime import datetime

# Create your models here.
class Category(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=255)

    def __str__(self)-> str:
        return self.title

# The Menu Items For The Restaurant
class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)

# The Comments from the users
class UserComment(models.Model):
    time_log = models.DateTimeField(default=datetime.now, editable=False)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    comment = models.TextField(max_length=1000)

