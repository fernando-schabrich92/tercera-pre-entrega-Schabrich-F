from django.shortcuts import render
from articulo.models import Entrada
from articulo.models import Datos
from django.db.models import Q
from django.http import HttpResponse
# Create your views here.
def home(request):

	articulos = Entrada.objects.all()
	if request.method == "POST":
	   nombre = request.POST["nombre"]
	   infocontacto = request.POST["infocontacto"]
	   obj = Datos(nombre=nombre,infocontacto=infocontacto)
	   obj.save()
	   mensaje = "Gracias por contactarte"
	   return render(request,"index.html",{"articulos":articulos,"mensaje":mensaje})

	return render(request,"index.html",{"articulos":articulos})

def programacionavanzada(request):
	articulos = Entrada.objects.all()
	if request.method == "POST":
	   nombre = request.POST["nombre"]
	   infocontacto = request.POST["infocontacto"]
	   obj = Datos(nombre=nombre,infocontacto=infocontacto)
	   obj.save()
	   mensaje = "Gracias por contactarte"
	   return render(request,"Programacionavanzada.html",{"articulos":articulos,"mensaje":mensaje})
	return render(request,"Programacionavanzada.html",{"articulos":articulos})


def programacioninicial(request):
	articulos = Entrada.objects.all()
	if request.method == "POST":
	   nombre = request.POST["nombre"]
	   infocontacto = request.POST["infocontacto"]
	   obj = Datos(nombre=nombre,infocontacto=infocontacto)
	   obj.save()
	   mensaje = "Gracias por contactarte"
	   return render(request,"ProgramacionInicial.html",{"articulos":articulos,"mensaje":mensaje})
	return render(request,"ProgramacionInicial.html",{"articulos":articulos})

def recursosbasicos(request):
	articulos = Entrada.objects.all()
	if request.method == "POST":
	   nombre = request.POST["nombre"]
	   infocontacto = request.POST["infocontacto"]
	   obj = Datos(nombre=nombre,infocontacto=infocontacto)
	   obj.save()
	   mensaje = "Gracias por contactarte"
	   return render(request,"RecursosBasicos.html",{"articulos":articulos,"mensaje":mensaje})
	return render(request,"RecursosBasicos.html",{"articulos":articulos})

def reparaciondeHarwareySoftware(request):
	articulos = Entrada.objects.all()
	return render(request,"Buscaturegistro.html",{"articulos":articulos})


def busqueda(request):
		mensaje="nombre buscado: %r"  %request.GET["no"]
		NOMBRE=request.GET["no"]
		dato=Datos.objects.filter(nombre__icontains=NOMBRE)


		return render(request, "index.html", {"NOMBRE": NOMBRE, "query": mensaje})










