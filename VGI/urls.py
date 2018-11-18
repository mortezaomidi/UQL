from django.conf.urls import include, url
from djgeojson.views import GeoJSONLayerView
from .import models

from .import views

urlpatterns = [
    url('accounts/', include('django.contrib.auth.urls')),
    url('home/', views.home, name="home"),
    url(r'^data/region.geojson$', GeoJSONLayerView.as_view(model=models.Region), name='data_region'),
    url(r'^data/unit.geojson$', GeoJSONLayerView.as_view(model=models.Unit, properties=('name',)), name='data_unit'),
    url(r'^data/criteria.geojson$', GeoJSONLayerView.as_view(model=models.Criteria, properties=('create_date',)), name='data_criteria'),
]
