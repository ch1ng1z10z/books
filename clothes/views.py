
from django.views.generic import ListView
from .models import Product


class AllProductsView(ListView):
    model = Product
    template_name = 'clothes/all_products.html'
    context_object_name = 'products'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Product.objects.filter(title__icontains=query)
        return Product.objects.all()


class MaleClothesView(ListView):
    model = Product
    template_name = 'clothes/male_clothes.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(category='male')


class FemaleClothesView(ListView):
    model = Product
    template_name = 'clothes/female_clothes.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(category='female')


class KidsClothesView(ListView):
    model = Product
    template_name = 'clothes/kids_clothes.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(category='kids')
