
from django.urls import path
from .views import AllProductsView, MaleClothesView, FemaleClothesView, KidsClothesView

urlpatterns = [
    path('', AllProductsView.as_view(), name='all_products'),
    path('male/', MaleClothesView.as_view(), name='male_clothes'),
    path('female/', FemaleClothesView.as_view(), name='female_clothes'),
    path('kids/', KidsClothesView.as_view(), name='kids_clothes'),
]
