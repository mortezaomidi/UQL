from django.conf.urls import include, url

from .import views

urlpatterns = [
    url('accounts/', include('django.contrib.auth.urls')),
    url('add/', views.PersonCreateView.as_view(), name='add'),
    url('home/', views.index, name='home'),

]
