from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Restaurant, Menu, MenuOption, Review


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'email', 'groups')


class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'address', 'open_time', 'close_time', 'is_dead', 'is_selectable_ingredients')


class MenuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Menu
        fields = ('id', 'restaurant', 'option', 'name')


class MenuOptionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MenuOption
        fields = ('id', 'name')


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'restaurant', 'menu', 'title', 'content', 'score', 'is_blind')
