from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse
from chat_incidentes.models import Incidentes
from django.utils import timezone

#Crear una clase persona
class Persona(object):
    def __init__(self, nombre, apellido) -> None:
        self.nombre=nombre
        self.apellido=apellido
        pass


#Crear una funcion, esto será una vista
def acerca(request):
    #Crear un objeto tipo Personna
    p1=Persona("Fernando","Avilés")

    #Crear una lista
    temas=["Aplicativo para monitorear incidentes Dirios", 
        "Modelos para registrar áreas, aplicativos y células", 
        "Formulario de gestión de Inc, Aplicativos", 
        "Vistas de control y revisión de aplicaciones", 
        "Despliegue"]
    
 
    
    #Diccionario con lo que vamos a pasar al render
    diccionario={"nombre_p":p1.nombre, "apellido_p":p1.apellido, "lista_temas":temas}

    return render(request, "acerca_de.html", diccionario)

#Crear otra vista
def despedida(request):
    color=[]
    duracion=[]
    incidentes_dia=Incidentes.objects.all()
    for i in incidentes_dia:
        color.append("whitesmoke")
        if i.horafin:
            duracion.append(i.horafin-i.horainicio)
        else:
            duracion.append(timezone.now()-i.horainicio)
    return render(request, "tablero.html",{'incidentes_dia':zip(incidentes_dia,color,duracion)})
    

def calculaEdad(request,edad, anno):#Pasar parametros por URL. Calcular una edad en año determinado
    
    periodo=anno-2022
    edadFut=edad+periodo
    imprimir="<h2>En el año %s tendrás %s años de edad</h2>"%(anno, edadFut)
    return HttpResponse(imprimir)

def home(request):    
    return render(request, "home.html")