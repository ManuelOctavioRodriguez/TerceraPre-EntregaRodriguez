from django.template import Template, Context
from django.template import loader
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse

def common(request):
    return HttpResponse("<strong> Common </strong> <br><br> La hoja en blanco de los anónimos")

def EnBlanco(self):
    miHtml = open("C:\\Users\\manuo\\OneDrive\\TerceraEntrega\\TercerProyecto\\Plantillas\\templates.html")
    plantilla = Template(miHtml.read())
    
    miHtml.close()
    miContexto = Context()
    
    documento = plantilla.render(miContexto)
    return HttpResponse(documento)

loader.get_template('templates.html')

