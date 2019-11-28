from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer, PostSerializer
from .models import Post

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PostView(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()