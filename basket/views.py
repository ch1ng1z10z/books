from django.shortcuts import render, get_object_or_404, redirect
from .models import Order
from books.models import Book

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'basket/order_list.html', {'orders': orders})

def add_order(request):
    if request.method == 'POST':
        name = request.POST.get('customer_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        book_id = request.POST.get('book')
        quantity = request.POST.get('quantity')
        book = get_object_or_404(Book, id=book_id)
        Order.objects.create(
            customer_name=name, email=email, phone=phone, address=address,
            book=book, quantity=quantity
        )
        return redirect('order_list')
    books = Book.objects.all()
    return render(request, 'basket/add_order.html', {'books': books})

def edit_order(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        order.customer_name = request.POST.get('customer_name')
        order.email = request.POST.get('email')
        order.phone = request.POST.get('phone')
        order.address = request.POST.get('address')
        order.book_id = request.POST.get('book')
        order.quantity = request.POST.get('quantity')
        order.save()
        return redirect('order_list')
    books = Book.objects.all()
    return render(request, 'basket/edit_order.html', {'order': order, 'books': books})

def delete_order(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order.delete()
    return redirect('order_list')
