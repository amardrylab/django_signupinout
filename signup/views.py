from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

# Create your views here.

class SignupView(CreateView):
	form_class=UserCreationForm
	template_name='registration/signup.html'
	success_url='/success/'
