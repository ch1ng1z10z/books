from django.urls import path
from .views import (
    BookListView, BookDetailView, CurrentTimeView,
    RandomNumberView, AboutMeView
)

urlpatterns = [
    path('time/', CurrentTimeView.as_view(), name='current_time'),
    path('random/', RandomNumberView.as_view(), name='random_number'),
    path('about/', AboutMeView.as_view(), name='about_me'),
    path('books/', BookListView.as_view(), name='book_list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
]
