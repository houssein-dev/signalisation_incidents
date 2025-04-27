from django.contrib import admin
from .models import Catagorie,Incident, Utilisateur
# Register your models here.

admin.site.register(Catagorie)
admin.site.register(Utilisateur)

class IncidentAdmin(admin.ModelAdmin):
    list_display=('longitude', 'latitude' , 'catagorie')
    list_filter=('catagorie',)
admin.site.register(Incident,IncidentAdmin)

 