from django.db import models

# Create your models here.
class MenuCategory(models.Model):
    menu_category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.menu_category_name

class Menu(models.Model):
    menu_item = models.CharField(max_length=200)
    price = models.IntegerField(null=False)
    category_id = models.ForeignKey(MenuCategory, on_delete=models.PROTECT, default=None, related_name="category_name")

    def __str__(self):
        return self.menu_item

class Working_Station(models.Model):
    working_area = models.CharField(max_length=200)

    def __str__(self):
        return self.working_area

class Shifts(models.Model):
    time_allocated = models.CharField(max_length=200)
    time_in = models.TimeField(null=False)
    time_out = models.TimeField(null=False)

    def __str__(self):
        return self.time_allocated

class Personel(models.Model):
    full_name = models.CharField(max_length=200)
    phone_number = models.IntegerField(null=True)
    age = models.IntegerField(null=False)
    sex = models.CharField(max_length=1,default="M", null = True)
    availability = models.BooleanField(null=True)
    duty_station = models.ForeignKey(Working_Station, on_delete=models.PROTECT, default=1)
    shift = models.ForeignKey(Shifts, on_delete=models.PROTECT, default="1")

    def __str__(self):
        return self.full_name


