# Imports
# -------------------------------------------------
# 3rd Parties:-
from django.urls import path

# internal:
from comments import views
# -------------------------------------------------

urlpatterns = [
    path('comments/', views.CommentList.as_view()),
    path('comments/<int:pk>/', views.CommentDetail.as_view()),
]