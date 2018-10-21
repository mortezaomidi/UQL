from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.http import HttpResponse
from django.urls import reverse_lazy
from . models import Criteria

class PersonCreateView(CreateView):
	model = Criteria
	fields = '__all__'
	success_url = reverse_lazy('home')


def index(request):
	pass
