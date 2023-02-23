
from flask import Flask
from flask import request
from flask import render_template
import forms  
from flask_wtf.csrf import CSRFProtect
from collections import Counter
from flask import make_response
from flask import flash

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

@app.route("/", methods=['GET','POST'])
def cajasDinamicas():
    reg_alum=forms.UserForm(request.form)
    if request.method == 'POST':
        numero=int(reg_alum.numero.data)
        return render_template("CajasDinamicas.html",numero=numero,form=reg_alum)
    else:
        return render_template("CajasDinamicas.html",form=reg_alum)

@app.route("/resultados", methods=['GET','POST'])
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
    datos=list()
    if request.method=='POST' and reg_tradu.validate():
        español=(str(datos.append(reg_tradu.español.data)))
        ingles=(str(datos.append(reg_tradu.ingles.data)))
        f=open('traductor.txt','a')
        f.write(str('\n'+datos[0]))
        f.write(str('\n'+datos[1]))

    return render_template("Traductor.html",form=reg_tradu,datos=datos)

@app.route("/cookie", methods=['GET','POST'])
def cookie():
    reg_user=forms.LoginForm(request.form)
    response=make_response(render_template('cookie.html',form=reg_user))

    if request.method=='POST' and reg_user.validate():
        user=reg_user.username.data
        password=reg_user.password.data
        datos=user+'@'+password
        success_message='Bienvenido {}'.format(user)
        response.set_cookie('datos_usuario',datos)
        flash(success_message)
    return response

if __name__=="__main__":
    csrf.init_app(app)
    app.run(debug=True,port=3000)