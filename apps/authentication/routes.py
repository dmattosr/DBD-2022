# -*- encoding: utf-8 -*-


'''
Copyright (c) 2019 - present AppSeed.us.
'''

from flask import render_template, redirect, request, url_for
from flask_login import (
    current_user,
    login_user,
    logout_user
)

from apps import db, login_manager
from apps.authentication import blueprint
from apps.authentication.forms import LoginForm, CreateAccountForm
from apps.authentication.models import Users
from apps.utils import constants

from sqlalchemy import text

from apps.authentication.util import verify_pass


@blueprint.route('/')
def route_default():
    return redirect(url_for('authentication_blueprint.login'))

# Login & Registration


@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm(request.form)
    if 'login' in request.form:

        # read form data
        username = request.form['username']
        password = request.form['password']

        # Locate user
        user = Users.query.filter_by(username=username).first()

        # Check the password
        if user and verify_pass(password, user.password):

            login_user(user)

            return redirect(url_for('authentication_blueprint.route_default'))

        # Something (user or pass) is not ok
        return render_template(
            'accounts/login.html',
            msg='Usuario o contraseña incorrectos',
            form=login_form,
        )

    if not current_user.is_authenticated:
        return render_template('accounts/login.html',
                               form=login_form)
    return redirect(url_for('home_blueprint.index'))


@blueprint.route('/register', methods=['GET', 'POST'])
def register():
    create_account_form = CreateAccountForm(request.form)
    if 'register' in request.form:
        cnx = db.engine.connect()

        sql = text('''
        SELECT *
        FROM departamento
        WHERE true;
        ''')
        res = cnx.execute(sql).fetchall()
        tipo_documento = request.form['tipo_documento']
        numero_documento = request.form['numero_documento']
        email = request.form['email']
        usuario = request.form['usuario']

        # Verifica que no exista el paciente existe con el tipo y numero de documento
        sql = '''
        SELECT true
        FROM paciente
        INNER JOIN persona ON persona.id_persona=paciente.id_persona
        WHERE true
            AND (persona.tipo_documento=:tipo_documento AND persona.numero_documento =:numero_documento)
            OR paciente.usuario=:usuario
        LIMIT 1;
        '''
        paciente = cnx.execute(
            text(sql),
            tipo_documento=tipo_documento,
            numero_documento=numero_documento,
            usuario=usuario,

        ).fetchone()

        if paciente:
            return render_template('accounts/register.html',
                                   msg='El paciente ya existe',
                                   success=False,
                                   form=create_account_form)

        # Verifica que el email de paciente sea único
        sql = '''
        SELECT true
        FROM paciente
        INNER JOIN persona ON persona.id_persona=paciente.id_persona
        WHERE true
            AND persona.email=:email
        '''
        paciente = cnx.execute(text(sql), email=email).fetchone()
        if paciente:
            return render_template('accounts/register.html',
                                   msg='Email ya ha sido registrado',
                                   success=False,
                                   form=create_account_form)

        # Creacion del paciente
        sql = '''
        INSERT INTO persona (
            id_persona,
            tipo_documento,
            numero_documento,
            apellido_paterno,
            apellido_materno,
            nombres,
            fecha_nacimiento,
            sexo,
            email,
            celular,
            fecha_registro,
            id_pais,
            id_distrito,
            direccion)
        VALUES (
            nextval('persona__id_persona'),
            :tipo_documento,
            :numero_documento,
            :apellido_paterno,
            :apellido_materno,
            :nombres,
            :fecha_nacimiento,
            :sexo,
            :email,
            :celular,
            now(),
            :id_pais,
            :id_distrito,
            :direccion
        )
        RETURNING id_persona;
        '''
        res_persona = cnx.execute(text(sql), **request.form).fetchone()

        sql = '''
        INSERT INTO paciente (
            id_persona,
            esta_activo,
            tipo_seguro,
            usuario,
            password
        ) values (
            :id_persona,
            1,
            :tipo_seguro,
            :usuario,
            :password
        );
        '''
        vals = {
            'id_persona': res_persona[0],
            'tipo_seguro': constants.TIPOSEGURO_NINGUNO,
            'usuario': request.form['usuario'],
            'password': request.form['password'],
        }
        res = cnx.execute(text(sql), **vals)

        user = Users(
            username=request.form['usuario'],
            email=request.form['email'],
            password=request.form['password'],
        )
        db.session.add(user)
        db.session.commit()

        # Delete user from session
        logout_user()

        return render_template('accounts/register.html',
                               msg='Paciente creado correctamente',
                               success=True,
                               form=create_account_form)

    else:
        return render_template('accounts/register.html', form=create_account_form)


@blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('authentication_blueprint.login'))

# Errors


@login_manager.unauthorized_handler
def unauthorized_handler():
    return render_template('home/page-403.html'), 403


@blueprint.errorhandler(403)
def access_forbidden(error):
    return render_template('home/page-403.html'), 403


@blueprint.errorhandler(404)
def not_found_error(error):
    return render_template('home/page-404.html'), 404


@blueprint.errorhandler(500)
def internal_error(error):
    return render_template('home/page-500.html'), 500
