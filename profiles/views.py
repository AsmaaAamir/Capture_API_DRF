# Imports
# -------------------------------------------------
# 3rd Parties:-
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response 

# internal:
from .models import Profile
from .serializers import ProfileSerializer
from capture.permissions import IsOwnerOrReadOnly
# -------------------------------------------------


class ProfileList(APIView):
    """
    Created a class to view all Profile's in a list
    """
    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)




class ProfileDetail(APIView):
    """
    Created a class to edit profile's 
    """
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]


    def get_object(self, pk):
        try:
            profile = Profile.objects.get(pk=pk)
            self.check_object_permissions(self.request, profile)
            return profile
        except Profile.DoesNotExist:
            raise Http404


    def get(self, request, pk):
        profile = self.get_object(pk)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)


    def put(self, request, pk):
        profile = self.get_object(pk)
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)