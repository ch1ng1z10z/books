from django.contrib import admin
from .models import Product, Tag

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')
    list_filter = ('category', 'tags')
    search_fields = ('title', 'description')

admin.site.register(Tag)
