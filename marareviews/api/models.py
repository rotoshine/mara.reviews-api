from django.db import models


# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=100)
    latitude = models.FloatField(null=True, blank=True, default=None)
    longitude = models.FloatField(null=True, blank=True, default=None)
    open_time = models.DateTimeField(null=True)
    close_time = models.DateTimeField(null=True)
    is_dead = models.BooleanField(default=False)
    is_selectable_ingredients = models.BooleanField(default=False)


class MenuOption(models.Model):
    name = models.CharField(max_length=20)


class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    option = models.ForeignKey(MenuOption, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)


class Review(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    content = models.TextField()
    score = models.PositiveSmallIntegerField()
    is_blind = models.BooleanField


