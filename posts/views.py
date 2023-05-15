# Imports
# -------------------------------------------------
# 3rd Parties:-
from rest_framework import generics, permissions

# internal:
from .models import Post
from .serializers import PostSerializer
from capture.permissions import IsOwnerOrReadOnly
# -------------------------------------------------


class PostList(generics.ListCreateAPIView):
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



class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    In post detail you can search post via ID and edit or delete post. 
    But only the auth user can edit or delets the post
    """
    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Post.objects.all()