from django.forms import ModelForm
from .models import Product
class  AddProductForm(ModelForm):
    class Meta:
        model = Product
        fields  = ['title' , 'description' , 'price', 'brand' , 'image']

