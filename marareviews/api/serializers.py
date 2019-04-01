from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Restaurant, Menu, MenuOption, Review


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'email', 'groups')


class MenuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Menu
        fields = ('id', 'option', 'name')


class RestaurantSerializer(serializers.ModelSerializer):
    menus = MenuSerializer(read_only=True, many=True)

    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'menus', 'address', 'open_time', 'close_time', 'is_dead', 'is_selectable_ingredients')


class MenuOptionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MenuOption
        fields = ('id', 'name')


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'restaurant', 'menu', 'title', 'content', 'score', 'is_blind')
