from django.db import models

# Create your models here.

class Aplicacion(models.Model):
    nom_app=models.CharField(max_length=30, verbose_name="Nombre")
    desc_app=models.CharField(max_length= 255, verbose_name="Descripción")
    celula=models.CharField(max_length= 30, verbose_name="Célula")

    def __str__(self) -> str:
        return (self.nom_app)#'--> %s'%

class Incidentes(models.Model):
    num_inc=models.CharField(max_length= 15)
    app_inc=models.ForeignKey(Aplicacion, on_delete=models.DO_NOTHING)
    titulo_inc=models.CharField(max_length= 100)
    rep_inc=models.CharField(max_length= 100)
    desc_inc=models.CharField(max_length=500)
    horainicio = models.DateTimeField(db_column='HoraInicio') 
    horafin = models.DateTimeField(db_column='HoraFin', blank=True, null=True)  
    esc_inc=models.CharField(max_length=50)
    critico=models.BooleanField()

    def __str__(self):
        return 'Número: %s Aplicativo: %s Hora Inicio: %s' % (self.num_inc, self.app_inc, self.horainicio)

class Areas(models.Model):
    nom_area=models.CharField(max_length=100)
    def __str__(self) -> str:
        return (self.nom_area)
    