# Imports
# -------------------------------------------------
# 3rd party: 
from rest_framework import generics, permissions 

# internal: 
from capture.permissions import IsOwnerOrReadOnly 
from likes.models import Like 
from likes.serializers import LikeSerializer 

 # -------------------------------------------------

class LikeList(generics.ListCreateAPIView): 
    """ 
    Users are able to list and create likes 
    """ 
    serializer_class = LikeSerializer 
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] 
    queryset = Like.objects.all() 
    
    def perform_create(self, serialiser): 
        serializer.save(owner=self.request.user) 

 
class LikeDetail(generics.RetrieveDestroyAPIView):
    """
    Users are able to retrieve and delete a like by id. 
    """
    serializer_class = LikeSerializer 
    permission_classes = [IsOwnerOrReadOnly] 
    queryset = Like.objects.all() 