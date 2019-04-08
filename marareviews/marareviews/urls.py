from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'restaurants', views.RestaurantViewSet)
router.register(r'menus', views.MenuViewSet)
router.register(r'menu-options', views.MenuOptionViewSet)
router.register(r'reviews', views.ReviewViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin', admin.site.urls),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework'))
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
