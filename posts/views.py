# Imports
# -------------------------------------------------
# 3rd Parties:-
from django.http import Http404
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response 

# internal:
from .models import Post
from .serializers import PostSerializer
from capture.permissions import IsOwnerOrReadOnly
# -------------------------------------------------


class PostList(APIView):
    """
    In post list, you will be abel to view all posts in a list 
    and add posts to. Also added permissions so only the auth user 
    can add the posts
    """
    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Post.objects.all()
   

   def perform_create(self, serializer):
    serializer.save(owner=self.request.user)



class PostDetail(APIView):
    """
    In post detail you can search post via ID and edit or delete post. 
    But only the auth user can edit or delets the post
    """
    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Post.objects.all()