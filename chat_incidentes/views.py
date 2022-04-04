from dataclasses import dataclass
import datetime
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils import timezone
from django.http import HttpResponse
from django.shortcuts import redirect, render
from chat_incidentes.forms import Form_Aplicacion, Form_Incidentes
from chat_incidentes.models import Aplicacion, Incidentes
import os #Importacion para copiar en portapapeles

# Create your views here.

def addToClipBoard(text):
    #command = 'echo | set /p nul=' + text.strip()+ '| clip'
    command = 'echo ' + text.strip()+ '| clip'
    
    os.system(command)


def incidentes(request):
    if request.method=="POST":
        form_incidente=Form_Incidentes(request.POST)
        if form_incidente.is_valid():
            #Crear Objeto Incidente
            incidente=Incidentes()
            #Agregar a los atributos los datos del formulario
            incidente.num_inc=form_incidente.cleaned_data['num_inc']
            incidente.app_inc=form_incidente.cleaned_data['app_inc']
            incidente.titulo_inc=form_incidente.cleaned_data['titulo_inc']
            incidente.rep_inc=form_incidente.cleaned_data['rep_inc']
            incidente.desc_inc=form_incidente.cleaned_data['desc_inc']
            incidente.horainicio =form_incidente.cleaned_data['horainicio']
            incidente.horafin =form_incidente.cleaned_data['horafin']
            incidente.esc_inc=form_incidente.cleaned_data['esc_inc']
            incidente.critico=form_incidente.cleaned_data['critico']
            incidente.save()
            #HttpResponse("Incidente "+incidente.num_inc+" guardado")
            return render(request, "detalle_inc.html",{"inc_saved":incidente})#redirect("/")
    else:
        #form_incidente=Form_Incidentes({'esc_inc':'SONDA'})
        form_incidente=Form_Incidentes()
    return render(request, "genera_chat.html",{"form":form_incidente} )

def aplicaciones(request):
    if request.method=="POST":
        form_aplicacion=Form_Aplicacion(request.POST)
        if form_aplicacion.is_valid():
            info_app=form_aplicacion.cleaned_data
            
            #Insertar en BD en Aplicaciones
            Aplicacion.objects.create(
            nom_app=info_app['nom_app'], 
            desc_app=info_app['desc_app'], 
            celula=info_app['celula'])
            publicacion_wsp="*"+info_app['nom_app']+"* *"+info_app['celula']+"* "+info_app['desc_app']
            print(publicacion_wsp, end="*")
            addToClipBoard(publicacion_wsp)
            return redirect("/")
    else:
        form_aplicacion=Form_Aplicacion()
    return render(request, "aplicaciones.html",{"form":form_aplicacion})


def tablero(request):
    #Definir parametros de inicio y fin del día
    today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
    today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
    incidentes_dia=Incidentes.objects.filter(horainicio__range=(today_min, today_max)).order_by('horainicio')
    color=[]
    duracion=[]
    for i in incidentes_dia:
        if i.horafin:
            color.append("table-dark")#Color Cerrado #BFC9CA
            duracion.append(i.horafin-i.horainicio)
        else:
            dif=(timezone.now()-i.horainicio).seconds #Se debe dejar el TZ como falso en settings
            duracion.append(timezone.now()-i.horainicio)
            if dif < 7200:
                color.append("table-success")#Color Normal #2ECC71
                
            elif dif < 14400:
                color.append("table-warning")#Color Alerta #F39C12
            else:
                color.append("table-danger")#Color Peligro #E74C3C
            #print("SEGUNDOS PASADOS: "+str(dif)+" -->HORA INICIAL %s AHORA %s"%(str(i.horainicio),str(timezone.datetime.now())))
    return render(request, "tablero.html",{"incidentes_dia":zip(incidentes_dia,color,duracion)})

def detalle_inc(request, inc):
    inc_detalle=Incidentes.objects.filter(num_inc=inc)
    return render(request, "detalle_inc.html",{'inc_detallado':inc_detalle})


class AplicacionesList(ListView):
    model=Aplicacion
    template_name="aplicaciones_list.html"

class AplicacionCreate(CreateView):
    model=Aplicacion
    form_class=Form_Aplicacion
    template_name='aplicaciones.html'
    success_url=reverse_lazy("listapp")

class AplicacionActualiza(UpdateView):
    model=Aplicacion
    fields=['nom_app','desc_app','celula']
    #form_class=Form_Aplicacion
    template_name='editar_app.html'
    success_url=reverse_lazy("listapp")

class AplicacionEliminar(DeleteView):
    model=Aplicacion
    template_name='elimina_app.html'
    success_url=reverse_lazy("listapp")