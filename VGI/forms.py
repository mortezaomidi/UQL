from django.contrib.gis import forms as geoforms
from leaflet.forms.widgets import LeafletWidget
from .models import Criteria
from django.contrib.auth.models import User

fields_name = [
    'q11', 'q12', 'q13', 'q14', 'q15', 'q21', 'q22', 'q23', 'q24', 'q25',
    'q26', 'q27', 'q28', 'q29', 'q210', 'q31', 'q32', 'q33', 'q34', 'q35',
    'q36', 'q37', 'q38', 'q39', 'q310', 'q311', 'q312', 'q313', 'q314', 'q315',
    'q316', 'q317']

class CriteriaForm(geoforms.ModelForm):
    class Meta:
        model = Criteria
        exclude = ['user', 'unit']
        widgets = {field: geoforms.Select() for field in fields_name}
        #geoforms.RadioSelect()
        widgets['geom'] = LeafletWidget()
