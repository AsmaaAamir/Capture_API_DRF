# Imports
# -------------------------------------------------
# 3rd Parties:-
from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend

# internal:
from .models import Comment
from .serializers import CommentsSerializer, CommentDetailSerializer
from capture.permissions import IsOwnerOrReadOnly
# -------------------------------------------------


class CommentList(generics.ListCreateAPIView):
    """
    List of comments that can be viewed or created
    """
    serializer_class = CommentsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fileds = ['post']


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Allowing user to retrieving, updating and deleting comments
    """
    serializer_class = CommentDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Comment.objects.all()
    

