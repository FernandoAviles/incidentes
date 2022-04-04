from django.contrib import admin
from chat_incidentes.models import Aplicacion, Areas, Incidentes


class AplicacionAdmin(admin.ModelAdmin):
    list_display=("nom_app","celula")
    search_fields=("nom_app","celula")

class IncidentesAdmin(admin.ModelAdmin):
    list_display=("num_inc","app_inc","titulo_inc", "desc_inc")
    list_filter=("horainicio",)
    #date_hierarchy="horainicio"

# Register your models here.
admin.site.register(Aplicacion, AplicacionAdmin)
admin.site.register(Incidentes, IncidentesAdmin)
admin.site.register(Areas)