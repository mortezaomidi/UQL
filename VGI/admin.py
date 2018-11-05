from django.contrib.gis import admin
from .models import Criteria, MyUser, Region, Unit

#@admin.register() decorator performs the same function as the admin.site.register()
@admin.register(Criteria)
class PostAdmin(admin.BingGeoAdmin):
    list_display = ([f.name for f in Criteria._meta.get_fields()])
    list_filter = ('create_date', 'user')
    #search_fields = ('name',)
    date_hierarchy = 'create_date'


admin.site.register(MyUser)
#admin.site.register(Criteria, admin.BingGeoAdmin)
admin.site.register(Region, admin.BingGeoAdmin)
admin.site.register(Unit, admin.BingGeoAdmin)
