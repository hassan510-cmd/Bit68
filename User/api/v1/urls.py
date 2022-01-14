from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet
from rest_framework.authtoken.views import ObtainAuthToken

router = DefaultRouter()

router.register('register', UserViewSet, basename='register')

urlpatterns = [
    path('', include(router.urls)),
    path('login', ObtainAuthToken.as_view()),
    path('my-product/', UserViewSet.get_seller_product),
]
