# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField
from wtforms.validators import Email, DataRequired
from sqlalchemy import text

from apps import db
from apps.utils import constants
# login and registration




class LoginForm(FlaskForm):
    username = StringField(
        'Usuario',
        id='username',
        validators=[DataRequired()])
    password = PasswordField(
        'Password',
        id='password',
        validators=[DataRequired()],
    )

class CreateAccountForm(FlaskForm):
    tipo_documento = SelectField(
        'Tipo de documento',
        id='tipo_documento',
        validators=[DataRequired()],
    )
    numero_documento = StringField(
        'Número de documento',
        id='numero_documento',
        validators=[DataRequired()])
    apellido_paterno = StringField(
        'Apellido Paterno',
        id='apellido_paterno',
        validators=[DataRequired()],
    )
    apellido_materno = StringField(
        'Apellido Materno',
        id='apellido_materno',
        validators=[DataRequired()],
    )
    nombres = StringField(
        'Nombres',
        id='nombres',
        validators=[DataRequired()],
    )
    sexo = SelectField(
        'Sexo',
        id='sexo',
        validators=[DataRequired()],
    )
    fecha_nacimiento = StringField(
        'Fecha de nacimiento',
        id='fecha_nacimiento',
        validators=[DataRequired()],
    )

    email = StringField(
        'Email',
        id='email',
        validators=[DataRequired(), Email()],
    )
    celular = StringField(
        'Celular',
        id='celular',
        validators=[DataRequired()],
    )
    direccion = StringField(
        'Direccion',
        id='direccion',
        validators=[DataRequired()],
    )
    id_pais = SelectField(
        'Nacionalidad',
        id='id_pais',
        validators=[DataRequired()],
    )
    id_distrito = SelectField(
        'Distrito',
        id='distrito_id',
        validators=[DataRequired()],
    )

    usuario = StringField(
        'Usuario',
        id='usuario',
        validators=[DataRequired()],)
    password = PasswordField(
        'Password',
        id='pwd_create',
        validators=[DataRequired()],
    )
    def __init__(self, *args, **kwargs):
        super(CreateAccountForm, self).__init__(*args, **kwargs)
        self.sexo.choices = [
            ('', 'Seleccione...'),
            (constants.SEXO_MASCULINO, 'Masculino'),
            (constants.SEXO_FEMENINO, 'Femenino'),
        ]

        self.tipo_documento.choices = [
            ('', 'Seleccione...'),
            (constants.TIPODOCUMENTO_DNI, 'Doc. Nacional de Identidad'),
            (constants.TIPODOCUMENTO_CE, 'Carnet de extranjería'),
        ]
        cnx = db.engine.connect()

        sql = '''
        SELECT id_pais,nombre from pais
        ORDER BY nombre;
        '''
        pais_list = cnx.execute(text(sql)).fetchall()

        self.id_pais.choices = [
            (item[0], item[1])
            for item in [('', 'Seleccione...'),] + pais_list
        ]

        sql = '''
        SELECT id_distrito, nombre, id_provincia from distrito
        ORDER BY nombre;
        '''
        distrito_list = cnx.execute(text(sql)).fetchall()

        self.id_distrito.choices = [
            (item[0], item[1])
            for item in distrito_list
        ]
