from django.conf.urls import include, url

from .import views

urlpatterns = [
    url('accounts/', include('django.contrib.auth.urls')),
    url('home/', views.home, name="home"),
]
