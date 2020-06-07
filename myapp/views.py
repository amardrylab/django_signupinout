from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Student

# Create your views here.


class StudentView(ListView):
	model=Student
	template_name='student_list.html'

class StudentCreate(LoginRequiredMixin, CreateView):
	model=Student
	fields=['name', 'marks']
