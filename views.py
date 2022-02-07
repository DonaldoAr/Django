from django.http import HttpResponse
from django.template import Template, Context
import datetime
# THE WAY TO LOAD A TEMPLATE
from django.template import loader

# FOR TO WRITE A MYNOR LINE'S CODE
from django.shortcuts import render


# THIS IS MY FIRST VIEW
def saludo(req):
    return HttpResponse("Hola mundo de Django")

def error404(req):
    return HttpResponse("Esta vista no esta disponible")

def giveFecha(req):
    fecha_actual = datetime.datetime.now()
    documento = """
        <html>
            <body>
                <h1>
                    Facha y hora actual: %s
                </h1>
            </body>
        </html>"""% fecha_actual
    return HttpResponse( documento )

def nombre(req, nombre, apellido):
    name = nombre
    lastName = apellido
    return HttpResponse("Tu nombre es: %s y apellido es: %s"%(name, lastName))

# USO DE PLANTILLAS
def saludoPlantilla(req):
    name = "Luis"
    nombre2 = "Donaldo"
    # doc_ext = open("./public/index.html")    
    # plt = Template( doc_ext.read() )
    # doc_ext.close()
    plantilla = loader.get_template('index.html')
    # ctx = Context( {
    #     "name": name,
    #     "name2": nombre2,
    #     "temas": ["platillas", "modelos", "formularios", "vistas", "desplieguess"]
    # } )
    dic = {
        "name": name,
        "name2": nombre2,
        "temas": ["platillas", "modelos", "formularios", "vistas", "desplieguess"]
    }
    document = plantilla.render( dic )
    return HttpResponse( document )

# EN EST RUTA SE USA shortcuts DE DJANGO PARA SIMPLIFICAR EL CODIGO
def main(req): 
    dic = { "user": ["Luis", "Donaldo"],
            "actividad": ["Prometeus", "Alien", "Anime"]}
    return render(req, 'main.html', dic)
    
    