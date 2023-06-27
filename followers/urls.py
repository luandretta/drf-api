from django.urls import path
from followers import views

urlpatterns = [
    path('followers', views.Follower.as_view()),
    path('followers/ < int:pk > /', views.FollowerDetail.as_view()),
]
