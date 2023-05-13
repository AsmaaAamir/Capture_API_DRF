# import
# -------------------------------------------------
# 3rd Parties:-
from django.urls import path

# internal: path('posts/<int:pk>/', views.PostDetail.as_view()),
from posts import views
# -------------------------------------------------


urlpatterns = [
    path('posts/', views.PostList.as_view()),
   
]