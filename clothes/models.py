from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY_CHOICES = (
        ('male', 'Одежда мужская'),
        ('female', 'Одежда женская'),
        ('kids', 'Детская одежда'),
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title

