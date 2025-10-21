from django.urls import path
from .views import OrderListView, OrderCreateView, OrderUpdateView, OrderDeleteView

urlpatterns = [
    path('', OrderListView.as_view(), name='order_list'),
    path('add/', OrderCreateView.as_view(), name='add_order'),
    path('<int:pk>/edit/', OrderUpdateView.as_view(), name='edit_order'),
    path('<int:pk>/delete/', OrderDeleteView.as_view(), name='delete_order'),
]
