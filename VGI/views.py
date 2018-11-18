from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from . models import Criteria
from .forms import CriteriaForm


def home(request):
    user = request.user
    if request.method == 'POST':
        form = CriteriaForm(request.POST)
        if form.is_valid():
            criteria = form.save(commit=False)
            criteria.user = user
            criteria.save()
            return HttpResponse('form is valid: and save. thanks')
    else:
        form = CriteriaForm()
    return render(request, 'VGI/home.html', {'form': form})
