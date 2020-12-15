from django.shortcuts import render , get_object_or_404 , redirect
from django.contrib.auth import get_user_model
from django.http import HttpResponseBadRequest

from .utils import send_confirmation_email
from .forms import SignUpForm
from .tokens import confirm_email_token_generator


User = get_user_model()

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
           user = form.save()
           user.as_active = False
           user.save()
           send_confirmation_email(request,user)
           return redirect('login')

    else:
        form = SignUpForm()

    return render (request , 'registration/signup.html', {'form':form})

def activate_email(request ,uid  ,token):
    user = get_object_or_404(User , pk=uid)
    if confirm_email_token_generator.check_token(user,token):
        user.is_active = True
        user.save()
        return redirect('login')
    else:
        HttpResponseBadRequest('Bad Token')
