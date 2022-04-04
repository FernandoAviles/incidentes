"""incidentes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from incidentes.view import calculaEdad, despedida, acerca, home
from chat_incidentes.views import AplicacionActualiza, aplicaciones, detalle_inc, incidentes, tablero, AplicacionesList, AplicacionCreate, AplicacionEliminar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('acerca/', acerca),
    path('despedida/',despedida),
    path('edades/<int:edad>/<int:anno>',calculaEdad),
    path('',home),
    path('registrar_inc/', incidentes),
    path('aplicaciones/', aplicaciones),
    path('listapp/', AplicacionesList.as_view(), name='listapp'),
    path('aplicacion/', AplicacionCreate.as_view(), name='ingresar'),
    path('app/<int:pk>', AplicacionActualiza.as_view(), name='actualiza'),
    path('eliminapp/<int:pk>', AplicacionEliminar.as_view(), name='elimina'),
    path('tablero/', tablero),
    path('incidente/<str:inc>', detalle_inc),
]
