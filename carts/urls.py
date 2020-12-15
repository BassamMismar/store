from django.urls import path
from .views import add_to_cart, cart


urlpatterns = [
    path('carts/', cart, name='cart'),
    path('carts/add/<int:product_id>', add_to_cart, name='add_to_cart'),
]
