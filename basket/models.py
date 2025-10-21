from django.db import models
from books.models import Book

class Order(models.Model):
    customer_name = models.CharField(max_length=100, verbose_name="Имя покупателя")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=20, verbose_name="Телефон", blank=True, null=True)
    address = models.TextField(verbose_name="Адрес доставки", blank=True, null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='orders', verbose_name="Книга")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Количество")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата заказа")

    def __str__(self):
        return f"Заказ {self.customer_name} — {self.book.title}"


