from django.urls import path
from . import views

urlpatterns = [
    path('time/', views.current_time, name='current_time'),
    path('random/', views.random_number, name='random_number'),
    path('about/', views.about_me, name='about_me'),
    path('books/', views.BookListView.as_view(), name='book_list'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
]
