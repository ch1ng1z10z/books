from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Order
from books.models import Book


class OrderListView(ListView):
    model = Order
    template_name = 'basket/order_list.html'
    context_object_name = 'orders'


class OrderCreateView(CreateView):
    model = Order
    template_name = 'basket/add_order.html'
    fields = ['customer_name', 'email', 'phone', 'address', 'book', 'quantity']
    success_url = reverse_lazy('order_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.all()
        return context


class OrderUpdateView(UpdateView):
    model = Order
    template_name = 'basket/edit_order.html'
    fields = ['customer_name', 'email', 'phone', 'address', 'book', 'quantity']
    success_url = reverse_lazy('order_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.all()
        return context


class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'basket/order_confirm_delete.html'  
    success_url = reverse_lazy('order_list')
