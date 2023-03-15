from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList,FormField, RadioField , SelectField
from wtforms.fields import EmailField
from wtforms import validators

def mi_validacion(form,field):
    if len(field.data)==0:
        raise validators.ValidationError('El campo no tiene datos')

class UserForm(Form):
    matricula=StringField('Matricula',
    [validators.DataRequired('El campo Matricula es requerido'),
    validators.length(min=5,max=10,message='Ingresa min 5 max 10')])
    nombre=StringField('nombre',[validators.DataRequired('El campo nombre es requerido')])
    apaterno=StringField('Apaterno',[mi_validacion])
    amaterno=StringField('Amaterno')
    email=EmailField('correo')
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

class ResistenciaForm(FlaskForm):
    opciones_banda = [("negro", "Negro"), ("marron", "Marrón"), ("rojo", "Rojo"), ("naranja", "Naranja"),
                      ("amarillo", "Amarillo"), ("verde", "Verde"), ("azul", "Azul"), ("violeta", "Violeta"),
                      ("gris", "Gris"), ("blanco", "Blanco")]

    opciones_tolerancia = [("oro", "Oro"), ("plata", "Plata")]

    banda1 = SelectField("Banda 1", choices=opciones_banda, validators=[validators.DataRequired()])
    banda2 = SelectField("Banda 2", choices=opciones_banda, validators=[validators.DataRequired()])
    banda3 = SelectField("Banda 3", choices=opciones_banda, validators=[validators.DataRequired()])
    tolerancia = RadioField("Tolerancia", choices=opciones_tolerancia, validators=[validators.DataRequired()])
    calcular = SubmitField("Calcular")
