# imports 
# -------------------------------------------------
# 3rd Parties:-
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from .settings import (JWT_AUTH_COOKIE, JWT_AUTH_REFRESH_COOKIE, JWT_AUTH_SAMESITE, JWT_AUTH_SECURE)



@api_view()
def root_route(request):
    return Response({
        "message" : "Hi there... :) This is Django REST Framework API for Capture"
    })

@api_view(['POST'])
def logout_route(request):
    response = Respone()
    response.set+cookie(
        key=JWT_AUTH_COOKIE,
        value='',
        httponly=True,
        expires='Thus, 01 Jan 1970 00:00:00 GMT',
        max_age=0,
        samesite=JWT_AUTH_SAMESITE,
        secure=JWT_AUTH_SECURE,
    )
    response.set_cookie(
        key=JWT_AUTH_REFRESH_COOKIE,
        value='',
        httponly=True,
        expires='Thus, 01 Jan 1970 00:00:00 GMT',
        max_age=0,
        samesite=JWT_AUTH_SAMESITE,
        secure=JWT_AUTH_SECURE,
    )
    return response
