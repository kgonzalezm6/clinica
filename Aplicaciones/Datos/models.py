from django.db import models

# Create your models here.
class Paciente(models.Model):
    Nombre=models.CharField(max_length=50)
    DPI=models.CharField(primary_key=True,max_length=13)
    Direccion=models.CharField(max_length=50)
    Fecha_Nacimiento=models.CharField(max_length=50)
    Razon_Visita=models.CharField(max_length=50)
    Numero=models.CharField(max_length=8)
    Otros=models.CharField(max_length=50)

    def __str__(self):
        texto= "{0} ({1})"
        return texto.format(self.Nombre, self.DPI) 

class Medico(models.Model):
    Nombre=models.CharField(max_length=50)
    Numero_Colegiado=models.CharField(primary_key=True,max_length=13)
    Especialidad=models.CharField(max_length=50)
    Diagnostico=models.CharField(max_length=50)
    Otros=models.CharField(max_length=50)

    def __str__(self):
        texto1= "{0} ({1})"
        return texto1.format(self.Nombre, self.Numero_Colegiado) 
    







