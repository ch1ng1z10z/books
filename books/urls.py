from django.urls import path
from .views import BookListView, BookDetailView, current_time, random_number, about_me

urlpatterns = [
    path('time/', current_time, name='current_time'),
    path('random/', random_number, name='random_number'),
    path('about/', about_me, name='about_me'),
    path('books/', BookListView.as_view(), name='book_list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
]
