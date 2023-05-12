# Imports
# -------------------------------------------------
# 3rd Parties:-
from rest_framework.views import APIView
from rest_framework.response import Response 

# internal:
from .models import Profile
from .serializers import ProfileSerializer
# -------------------------------------------------


class ProfileList(APIView):
    """
    Created a class view for the ProfileList
    """
    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)