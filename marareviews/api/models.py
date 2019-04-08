from django.db import models

from common.models import TimeStampedModel


class MenuOption(TimeStampedModel):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Menu(TimeStampedModel):
    option = models.ForeignKey(MenuOption, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name}-{self.option.name}'


class Restaurant(TimeStampedModel):
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=100)
    latitude = models.FloatField(null=True, blank=True, default=None)
    longitude = models.FloatField(null=True, blank=True, default=None)
    open_time = models.DateTimeField(null=True)
    close_time = models.DateTimeField(null=True)
    is_dead = models.BooleanField(default=False)
    is_selectable_ingredients = models.BooleanField(default=False)
    menus = models.ManyToManyField(Menu)

    def __str__(self):
        return self.name


class Review(TimeStampedModel):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    content = models.TextField()
    score = models.PositiveSmallIntegerField()
    is_blind = models.BooleanField

    def __str__(self):
        return self.title
