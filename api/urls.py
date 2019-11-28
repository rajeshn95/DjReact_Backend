from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import UserViewSet, PostView

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('posts', PostView )

urlpatterns = [
    path('', include(router.urls)),
]
