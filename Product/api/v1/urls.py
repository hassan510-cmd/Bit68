from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

router = DefaultRouter()

router.register('list', ProductViewSet, basename='list')

urlpatterns = [
    path('', include(router.urls)),
    # path('login',ObtainAuthToken.as_view())
]
