from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.movie_list, name='movie_list'),
    path('add/', views.add_movie, name='add_movie'),
    path('<int:pk>/edit/', views.edit_movie, name='edit_movie'),
    path('<int:pk>/delete/', views.delete_movie, name='delete_movie'),
]
