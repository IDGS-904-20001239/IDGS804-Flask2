from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList,FormField, RadioField 
from wtforms.fields import EmailField
from wtforms import validators

def mi_validacion(form,field):
    if len(field.data)==0:
        raise validators.ValidationError('El campo no tiene datos')

class UserForm(Form):
    matricula=StringField('Matricula',
    [validators.DataRequired(message='El campo Matricula es requerido'),
    validators.length(min=5,max=10,message='Ingesa un min 5 max 10')
                        ])
    nombre=StringField('Nombre',[validators.DataRequired(message='El campo Nombre es requerido')])
    apaterno=StringField('Apaterno',[
        mi_validacion
    ])
    amanterno=StringField('Amaterno')
    email=StringField('Correo')
    numero=StringField('Numero')

class TraduForm(Form):
    español=StringField('Español')
    ingles=StringField('Ingles')

class LoginForm(Form):
    username=StringField('Usuario',
    [validators.DataRequired(message='El campo Matricula es requerido'),
    validators.length(min=5,max=10,message='Ingesa un min 5 max 10')])
    password=StringField('Contraseña',
    [validators.DataRequired(message='El campo Contraseña es requerido'),
    validators.length(min=5,max=10,message='Ingesa un min 5 max 10')])
