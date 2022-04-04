import datetime
from django import forms
from django.utils import timezone
from chat_incidentes.models import Aplicacion, Areas



class Form_Incidentes(forms.Form):
    app_inc=forms.ModelChoiceField(label='APLICACIÓN', queryset=Aplicacion.objects.order_by('nom_app'))
    num_inc=forms.CharField(max_length=15, label='NÚMERO INCIDENTE')
    #app_inc=forms.ChoiceField(choices=opciones, label="APLICACIÓN")    
    titulo_inc=forms.CharField(label='TÍTULO')
    rep_inc=forms.ModelChoiceField(label='REPORTADO POR', queryset=Areas.objects.all().order_by('nom_area'))
    #rep_inc=forms.ChoiceField(label='REPORTADO POR', choices=reportado)
    desc_inc=forms.CharField(label='DESCRIPCIÓN', widget=forms.Textarea)
    horainicio =forms.DateTimeField(label='HORA INCIO', initial=timezone.now())# datetime.datetime.now()
    horafin =forms.DateTimeField(label='HORA FIN', required=False)
    esc_inc=forms.CharField(label='ESCALAMIENTO')
    critico=forms.BooleanField(required=False)

class Form_Aplicacion(forms.Form):
    nom_app=forms.CharField(label='NOMBRE APLICATIVO')
    desc_app=forms.CharField(label='DESCRIPCIÓN', widget=forms.Textarea)
    celula=forms.CharField(label='CÉLULA')

