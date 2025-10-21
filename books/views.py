
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, View
from datetime import datetime
import random
from .models import Book


class CurrentTimeView(View):
    def get(self, request, *args, **kwargs):
        now = datetime.now().strftime("%H:%M:%S")
        return HttpResponse(f"<h1>Текущее время: {now}</h1>")


class RandomNumberView(View):
    def get(self, request, *args, **kwargs):
        number = random.randint(1, 100)
        return HttpResponse(f"<h1>Случайное число: {number}</h1>")


class AboutMeView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("<h1>Я</h1><p>Чынгызхан</p>")


class BookListView(ListView):
    model = Book
    template_name = 'books1/book_list.html'
    context_object_name = 'books'


class BookDetailView(DetailView):
    model = Book
    template_name = 'books1/book_detail.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = self.object.reviews.all()
        context['average_rating'] = self.object.average_rating()
        return context

    def get_object(self, queryset=None):
        return get_object_or_404(Book, pk=self.kwargs.get('pk'))
