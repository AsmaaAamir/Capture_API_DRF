# Imports
# -------------------------------------------------
# 3rd Parties:-
from django.db.models import Count
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend

# internal:
from .models import Profile
from .serializers import ProfileSerializer
from capture.permissions import IsOwnerOrReadOnly
# -------------------------------------------------


class ProfileList(generics.ListAPIView):
    """
    Created a class to view all Profile's in a list
    """
    serializer_class = ProfileSerializer
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    ordering_fields = [
        'posts_count',
        'followers_count',
        'following_count',
        'owner__followed__created_at',
        'owner__following_created_at',
    ]
    filterset_fields = [
        'owner__following__followed__profile',
    ]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Created a class to edit profile's 
    """
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_at')