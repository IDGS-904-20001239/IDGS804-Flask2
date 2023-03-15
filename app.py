
from flask import Flask
from flask import request
from flask import render_template
import forms  
from flask_wtf.csrf import CSRFProtect
from collections import Counter
from flask import make_response
from flask import flash
import math
import json

import forms

app=Flask(__name__)
app.config['SECRET_KEY']="esta es una clave encriptada"
csrf=CSRFProtect()
@app.route("/formprueba")
def formprueba():
    return render_template("formprueba.html")

@app.route("/Alumnos", methods=['GET','POST'])
def alumnos():
    reg_alum=forms.UserForm(request.form)
    datos=list()
    if request.method=='POST' and reg_alum.validate():
        datos.append(reg_alum.matricula.data)
        datos.append(reg_alum.nombre.data)
        print(reg_alum.matricula.data)
        print(reg_alum.nombre.data)
    return render_template("Alumnos.html",form=reg_alum,datos=datos)

@app.route("/Caja", methods=['GET','POST'])
def cajasDinamicas():
    reg_alum=forms.UserForm(request.form)
    if request.method == 'POST':
        numero=int(reg_alum.numero.data)
        return render_template("CajasDinamicas.html",numero=numero,form=reg_alum)
    else:
        return render_template("CajasDinamicas.html",form=reg_alum)

@app.route("/resu", methods=['GET','POST'])
def calculos():
    reg_alum=forms.UserForm(request.form)
    lis= request.form.getlist("txtnum")

    maxim = int(lis[0])
    for x in lis:
        if int(maxim) > int(x):
            maxim = maxim
        else:
            maxim=x
   
    minimo = int(lis[0])
    for m in lis:
        if int(minimo) < int(m):
            minimo = minimo
        else:
            minimo=m
    suma=0
    for valor in lis:
        suma = suma + int(valor)
    cant = len(lis)
    promedio = suma / cant

    conteo=Counter(lis)
    resultado={}
    for n in conteo:  
        val=conteo[n]
        resultado[n] = val
    return render_template("resultado.html",lis=lis, maxim=maxim, minimo=minimo,promedio=promedio, resultado=resultado)
        
@app.route("/traductor", methods=['GET','POST'])
def tradu():
    reg_tradu=forms.TraduForm(request.form)
    palabraEncontrada = ''
    if(request.method == 'POST' and reg_tradu.validate()):
        btnGuardar = request.form.get('btnGuardar')
        btnTraducir = request.form.get('btnTraducir')
        if(btnGuardar == 'Guardar'):    
            file = open('traductor.txt', 'a')
            file.write('\n' + reg_tradu.español.data.upper() + '\n' + reg_tradu.ingles.data.upper())
            file.close()
        if(btnTraducir == 'Traducir'):
            opcion = request.form.get('translate')
            file = open('traductor.txt', 'r')
            palabras = [linea.rstrip('\n') for linea in file]
            if(opcion == 'spanish'):
                spanishWord = request.form.get('txtSpanish')
                for posicion in range(len(palabras)):
                    if(palabras[posicion] == spanishWord.upper()):
                        palabraEncontrada = palabras[posicion - 1]
                        break
                    else:
                        palabraEncontrada = 'No existe'
            elif(opcion == 'english'):
                englishWord = request.form.get('txtEnglish')
                for posicion in range(len(palabras)):
                    if(palabras[posicion] == englishWord.upper()):
                        palabraEncontrada = palabras[posicion + 1]
                        print(palabraEncontrada)
                        break
                    else:
                        palabraEncontrada = 'No existe'

    return render_template("Traductor.html",form=reg_tradu,palabraEncontrada = palabraEncontrada)

def calcular_resistencia(banda1, banda2, banda3, tolerancia):

    valores = {
        "negro": 0,
        "marron": 1,
        "rojo": 2,
        "naranja": 3,
        "amarillo": 4,
        "verde": 5,
        "azul": 6,
        "violeta": 7,
        "gris": 8,
        "blanco": 9
    }
    english_names = {
        "negro": "black",
        "marron": "brown",
        "rojo": "red",
        "naranja": "orange",
        "amarillo": "yellow",
        "verde": "green",
        "azul": "blue",
        "violeta": "violet",
        "gris": "gray",
        "blanco": "white",
        "oro": "gold",
        "plata": "silver"
    }
    banda1_en = english_names[banda1]
    banda2_en = english_names[banda2]
    banda3_en = english_names[banda3]
    tolerancia_en = english_names[tolerancia]

    valor1 = valores[banda1]
    valor2 = valores[banda2]
    multiplicador = math.pow(10, valores[banda3])
    tolerancia_valor = 0.05 if tolerancia == "oro" else 0.1

    valor = (valor1 * 10 + valor2) * multiplicador
    valor_minimo = valor * (1 - tolerancia_valor)
    valor_maximo = valor * (1 + tolerancia_valor)

    return {
        "colorBanda1": banda1_en,
        "colorBanda2": banda2_en,
        "colorBanda3": banda3_en,
        "colorTolerancia": tolerancia_en,
        "banda1": banda1,
        "banda2": banda2,
        "banda3": banda3,
        "tolerancia": tolerancia,
        "valor": valor,
        "valor_minimo": valor_minimo,
        "valor_maximo": valor_maximo
    }


@app.route('/', methods=['GET'])
def index():
    form = forms.ResistenciaForm(request.form)

    with open("Resistencia.txt", "r") as f:
        valores_guardados = [line.strip().split(",") for line in f]

    resultados_guardados = []
    for valores in valores_guardados:
        if len(valores) == 4:
            resultado_guardado = calcular_resistencia(*valores)
            resultados_guardados.append(resultado_guardado)

    return render_template('Resistencias.html', form=form, resultados_guardados=resultados_guardados)


@app.route('/', methods=['POST'])
def calcular():
    form =forms.ResistenciaForm(request.form)
    banda1 = request.form['banda1']
    banda2 = request.form['banda2']
    banda3 = request.form['banda3']
    tolerancia = request.form['tolerancia']

    resultado = calcular_resistencia(banda1, banda2, banda3, tolerancia)

    valores_guardados = []
    with open("Resistencia.txt", "r") as f:
        for line in f:
            valores = line.strip().split(",")
            if len(valores) == 4:
                resultado_guardado = calcular_resistencia(*valores)
                valores_guardados.append(resultado_guardado)
                print(valores_guardados)

    valores_guardados.append(resultado)

    with open("Resistencia.txt", "a") as f:
        f.write(",".join([banda1, banda2, banda3, tolerancia]) + "\n")

    return render_template('Resistencias.html', resultado=resultado, form=form, valores_guardados=valores_guardados)

if __name__=="__main__":
    csrf.init_app(app)
    app.run(debug=True,port=3000)