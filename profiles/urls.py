# Imports
# -------------------------------------------------
# 3rd Parties:-
from django.urls import path

# internal:
from profiles import views
# -------------------------------------------------




urlpatterns = [
    path('profiles/', views.ProfileList.as_view()),
]