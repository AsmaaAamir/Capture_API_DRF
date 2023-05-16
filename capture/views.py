# imports 
# -------------------------------------------------
# 3rd Parties:-
from rest_framework.decorators import api_view
from rest_framework.response import Response 


@api_view()
def root_route(request):
    return Response({
        "message" : "Hi there... :) This is Django REST Framework API for Capture"
    })