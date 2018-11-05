from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from . models import Criteria
from .forms import CriteriaForm










#////////////////////// not good ////////////
class PersonCreateView(CreateView):
	model = Criteria
	fields = '__all__'
	success_url = reverse_lazy('home')


#@login_required
def new_data(request):
    if request.method == 'POST':
        form = CriteriaForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save()
            return redirect('products_list')
    else:
        form = CriteriaForm()
    return render(request, 'VGI/add_data.html', {'form': form})
