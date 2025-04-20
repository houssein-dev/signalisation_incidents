from django.contrib import admin
from .models import Catagorie,Incident
# Register your models here.

admin.site.register(Catagorie)

class IncidentAdmin(admin.ModelAdmin):
    list_display=('longitude', 'latitude' , 'catagorie')
    list_filter=('catagorie',)
admin.site.register(Incident,IncidentAdmin)

