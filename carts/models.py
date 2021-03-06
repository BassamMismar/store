from django.db import models
from django.contrib.auth import get_user_model

from products.models import Product

User = get_user_model()

# Create your models here.


class Cart(models.Model):
    user = models.OneToOneField(User, related_name='cart' , on_delete=models.CASCADE)
    items = models.ManyToManyField(Product)
    update_at = models.DateTimeField(auto_now=True)
 
    def __str__(self):
        return str(self.user)

# @resicer(save_post, instance = User )
# def create_user_cart(request, )









    