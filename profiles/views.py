# Imports
# -------------------------------------------------
# 3rd Parties:-
from rest_framework import generice


# internal:
from .models import Profile
from .serializers import ProfileSerializer
from capture.permissions import IsOwnerOrReadOnly
# -------------------------------------------------


class ProfileList(APIView):
    """
    Created a class to view all Profile's in a list
    """
    serializer_class = ProfileSerializer
    queeryset = Profile.objects.all()


class ProfileDetail(APIView):
    """
    Created a class to edit profile's 
    """
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()
