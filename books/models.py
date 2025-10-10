from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Book(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название книги")
    description = models.TextField(verbose_name="Описание книги")
    image = models.ImageField(upload_to='books/', verbose_name="Обложка", blank=True, null=True)
    quantity_page = models.PositiveIntegerField(verbose_name="Количество страниц")
    author = models.CharField(max_length=255, verbose_name="Писатель")
    book_audio = models.URLField(verbose_name="Ссылка на аудиокнигу (YouTube)", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def average_rating(self):
        reviews = self.reviews.all()
        if reviews.exists():
            return round(sum(r.rating for r in reviews) / reviews.count(), 1)
        return 0

    def __str__(self):
        return self.title


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Отзыв на {self.book.title} — {self.rating}★"