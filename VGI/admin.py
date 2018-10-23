from django.contrib.gis import admin
from .models import Criteria, MyUser, Region, Unit

admin.site.register(MyUser)
admin.site.register(Criteria, admin.BingGeoAdmin)
admin.site.register(Region, admin.BingGeoAdmin)
admin.site.register(Unit, admin.BingGeoAdmin)
