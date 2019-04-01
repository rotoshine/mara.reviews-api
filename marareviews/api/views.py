from django.contrib.auth.models import User
from rest_framework import viewsets
from .models import Restaurant, Menu, MenuOption, Review
from .serializers import UserSerializer, RestaurantSerializer, MenuSerializer, MenuOptionSerializer, ReviewSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class MenuOptionViewSet(viewsets.ModelViewSet):
    queryset = MenuOption.objects.all()
    serializer_class = MenuOptionSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
