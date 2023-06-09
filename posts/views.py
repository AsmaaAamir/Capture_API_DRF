# Imports
# -------------------------------------------------
# 3rd Parties:-
from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend

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
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.annotate(
        comments_count=Count('comment', distinct=True),
        likes_count=Count('likes', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    ordering_fields = [
        'comments_count',
        'likes_count',
        'likes__created_at',
    ]
    search_fields = [
        'owner__username',
        'title',
        'category',
    ]

    filterset_fields =[
        'owner__followed__owner__profile',
        'likes__owner__profile',
        'owner__profile',
        'category',
    ] 

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    In post detail you can search post via ID and edit or delete post. 
    But only the auth user can edit or delets the post
    """
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.annotate(
        comments_count=Count('comment', distinct=True),
        likes_count=Count('likes', distinct=True)
    ).order_by('-created_at')