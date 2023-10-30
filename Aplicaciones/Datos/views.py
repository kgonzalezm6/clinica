from django.shortcuts import render, redirect
from .models import Paciente
from .models import Medico
from django.contrib import messages
# Create your views here.
def home(request):
    pacientesListados = Paciente.objects.all()
    medicosListados = Medico.objects.all()
    return render(request, "gestionPacientes.html",{"pacientes": pacientesListados,"medicos": medicosListados})   

def registrarPaciente(request):
    Nombre=request.POST['textNombre']
    DPI=request.POST['textDPI']
    Direccion=request.POST['textDireccion']
    Fecha_Nacimiento=request.POST['textFecha_Nacimiento']
    Razon_Visita=request.POST['textRazon_Visita']
    Numero=request.POST['textNumero']
    Otros=request.POST['textOtros']

    paciente=Paciente.objects.create(Nombre=Nombre,DPI=DPI,Direccion=Direccion,Fecha_Nacimiento=Fecha_Nacimiento,Razon_Visita=Razon_Visita,Numero=Numero,Otros=Otros)
    messages.success(request, '¡Paciente Registrado!')
    return redirect('/')

def edicionPaciente(request,DPI):
    paciente=Paciente.objects.get(DPI=DPI)
    return render (request, "edicionPaciente.html",{"paciente":paciente})

def editarPaciente(request):
    Nombre=request.POST['textNombre']
    DPI=request.POST['textDPI']
    Direccion=request.POST['textDireccion']
    Fecha_Nacimiento=request.POST['textFecha_Nacimiento']
    Razon_Visita=request.POST['textRazon_Visita']
    Numero=request.POST['textNumero']
    Otros=request.POST['textOtros']
    paciente=Paciente.objects.get(DPI=DPI)
    paciente.Nombre=Nombre
    paciente.DPI=DPI
    paciente.Direccion=Direccion
    paciente.Fecha_Nacimiento=Fecha_Nacimiento
    paciente.Razon_Visita=Razon_Visita
    paciente.Numero=Numero
    paciente.Otros=Otros
    paciente.save()
    messages.success(request, '¡Paciente Actualizado!')
    return redirect('/')

def eliminarPaciente(request,DPI):
    paciente=Paciente.objects.get(DPI=DPI)
    paciente.delete()
    messages.success(request, '¡Paciente Eliminado')
    return redirect('/')

def registrarMedico(request):
    Nombre=request.POST['textNombre']
    Numero_Colegiado=request.POST['textNumero_Colegiado']
    Especialidad=request.POST['textEspecialidad']
    Diagnostico=request.POST['textDiagnostico']
    Otros=request.POST['textOtros']

    medico=Medico.objects.create(Nombre=Nombre,Numero_Colegiado=Numero_Colegiado,Especialidad=Especialidad,Diagnostico=Diagnostico,Otros=Otros)
    messages.success(request, '¡Médico Registrado!')
    return redirect('/')

def eliminarMedico(request,Numero_Colegiado):
    medico=Medico.objects.get(Numero_Colegiado=Numero_Colegiado)
    medico.delete()
    messages.success(request, '¡Médico Eliminado')
    return redirect('/')

def edicionMedico(request,Numero_Colegiado):
    medico=Medico.objects.get(Numero_Colegiado=Numero_Colegiado)
    return render(request,"edicionMedico.html",{"medico":medico})

def editarMedico(request):
    Nombre=request.POST['textNombre']
    Numero_Colegiado=request.POST['textNumero_Colegiado']
    Especialidad=request.POST['textEspecialidad']
    Diagnostico=request.POST['textDiagnostico']
    Otros=request.POST['textOtros']
    medico=Medico.objects.get(Numero_Colegiado=Numero_Colegiado)
    medico.Nombre=Nombre
    medico.Numero_Colegiado=Numero_Colegiado
    medico.Especialidad=Especialidad
    medico.Diagnostico=Diagnostico
    medico.Otros=Otros
    medico.save()
    messages.success(request, '¡Médico Actualizado!')
    return redirect('/')


