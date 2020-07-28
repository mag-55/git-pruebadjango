from django.http import HttpResponse
import datetime
from django.template import Template, Context, loader
from django.shortcuts import render

class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre 
        self.apellido = apellido

def saludo(request):#CARGAR PLANTILLAS CON SHORTCUTS
    p1 = Persona("Profesor Juan", "Diaz")
    temas = ["Plantillas", "Modelos", "Formularios", "Vistas", "Despliegue"]
    ahora = datetime.datetime.now()
    return render(request, "miplantilla.html", {"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "momento_actual":ahora, "temas":temas})

def saludar(request):#CARGAR PLANTILLAS CON CARGADOR
    p1 = Persona("Profesor Juan", "Diaz")
    temas = ["Plantillas", "Modelos", "Formularios", "Vistas", "Despliegue"]
    ahora = datetime.datetime.now()
    doc_externo = loader.get_template('miplantilla.html')
    dic = {"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "momento_actual":ahora, "temas":temas}
    documento = doc_externo.render(dic)
    return HttpResponse(documento)

def saludos(request):#CARGAR PLANTILLAS DE FORMA MANUAL
    p1 = Persona("Profesor JOSE", "Diaz")
    #nombre = "Juan"
    #apellido = "Diaz"
    temas = ["Plantillas", "Modelos", "Formularios", "Vistas", "Despliegue"]
    ahora = datetime.datetime.now()
    #cargo documento externo html
    doc_externo = open("/home/mag/Plantillas/python/proyectos/prueba1/prueba1/plantillas/miplantilla.html")
    #cargo la plntilla
    plt = Template(doc_externo.read())
    doc_externo.close()
    #contex sirve para pasar variables y objetos via diccionarios 
    ctx = Context({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "momento_actual":ahora, "temas":temas})
    documento = plt.render(ctx)
    return HttpResponse(documento)

def despedida(reuqest):
    return HttpResponse("Hasta luego alumnos de Django")

def dame_fecha(request): #datos dinamicos, van cambiando en la pagina
    fecha_actual = datetime.datetime.now()
    documento = """<html>
                    <body>
                    <h2>Fecha y hora actuales %s</h2>
                    </body>
                </html>""" %fecha_actual
    return HttpResponse(documento)

def calcula_edad(request, edad, anio): #paso de parametros
    #edad_actual = 18
    periodo = anio - 2019
    edad_futura = edad + periodo
    documento = """<html>
                    <body>
                    <h2>En el año %s temdras %s años</h2>
                    </body>
                </html>""" %(anio, edad_futura)
    return HttpResponse(documento)

def cursoC(request):
    fecha_actual = datetime.datetime.now()
    return render(request, "CursoC.html", {"dameFecha":fecha_actual})

def cursoCss(request):
    fecha_actual = datetime.datetime.now()
    return render(request, "CursoCss.html", {"dameFecha":fecha_actual})
