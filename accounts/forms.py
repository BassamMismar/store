from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class SignUpForm(UserCreationForm):

    fristname = forms.CharField(max_length=30, required=False)
    lastname = forms.CharField(max_length=30, required=False)    
    email = forms.EmailField(max_length=254)    

    class Meta:
        model = User
        fields = (
            'username',
            'password1',
            'password2',
            'fristname',
            'lastname',
            'email'
        )
        

