# import
# -------------------------------------------------
# 3rd Parties:-
from django.urls import path

# internal:,
from likes import views
# -------------------------------------------------

urlpatterns = [
    path('likes/', views.LikeList.as_view()),
    path('likes/<int:pk>/', views.LikeDetail.as_views()),
]