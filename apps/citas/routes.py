# -*- encoding: utf-8 -*-

import os

from sqlalchemy import text
from werkzeug.utils import secure_filename

from flask import flash, render_template, redirect, request, url_for, Response, send_from_directory
from flask_login import current_user, login_required
from flask_paginate import Pagination, get_page_parameter

from apps.citas import blueprint
from apps import db
from run import app_config

from apps.utils import _default_uuid, constants

from .forms import CommentForm, StateForm




def allowed_file(filename, extension_list=False):
    extension_list = extension_list or app_config.ALLOWED_EXTENSIONS
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in extension_list


@blueprint.route('/nueva', methods=['GET'])
@login_required
def citas_nuevacita():
    class Constantes():
        SELEC_DISTRITO = 'selec_distrito'
        SELEC_ESTABLECIMIENTO = 'selec_establecimiento'
        SELEC_ESPECIALIDAD = 'selec_especialidad'
        SELEC_FECHA = 'selec_fecha'
    constantes = Constantes()

    opcion = request.args.get('opcion', type=str, default=constantes.SELEC_DISTRITO)
    id_distrito = request.args.get('id_distrito', type=str, default=False)
    id_estableciento = request.args.get('id_estableciento', type=str, default=False)
    id_especialidad = request.args.get('id_especialidad', type=str, default=False)
    data_list = []

    cnx = db.engine.connect()
    if opcion == constantes.SELEC_DISTRITO:
        sql = '''
        SELECT
            distrito.id_distrito,
            distrito.nombre distrito_nombre,
            count(*) total
        FROM establecimiento
        INNER join distrito on distrito.id_distrito=establecimiento.id_distrito
        GROUP by 1
        ORDER BY distrito.nombre
        '''
        data_list = cnx.execute(text(sql)).fetchall()

    elif opcion == constantes.SELEC_ESTABLECIMIENTO:
        sql = '''
        SELECT
            distrito.id_distrito,
            distrito.nombre distrito_nombre,
            establecimiento.id_estableciento,
            establecimiento.nombre,
            establecimiento.direccion,
            establecimiento.latitud,
            establecimiento.longitud
        FROM establecimiento
        INNER join distrito on distrito.id_distrito=establecimiento.id_distrito
        WHERE distrito.id_distrito=:id_distrito
        ORDER BY 2
        '''
        data_list = cnx.execute(text(sql), id_distrito=id_distrito).fetchall()

    elif opcion == constantes.SELEC_ESPECIALIDAD:
        sql = '''
        SELECT
            ee.id_estableciento,
            Especialidad.id_especialidad,
            Especialidad.nombre
        FROM Especialidad
        INNER JOIN EstablecimientoEspecialidad ee ON ee.id_especialidad=Especialidad.id_especialidad
        WHERE ee.id_estableciento=:id_estableciento
        ORDER BY Especialidad.nombre;
        '''
        data_list = cnx.execute(text(sql), id_estableciento=id_estableciento).fetchall()
    elif opcion == constantes.SELEC_FECHA:
        print('>>>> id_especialidad ZZZ', id_especialidad)
        sql = '''
        SELECT
            cita.fecha,
            cita.id_turno,
            consultorio.id_consultorio,
            turno.nombre  || ' de ' || turno.hora_inicio || ' ' || turno.hora_final nombre,
            cita.fecha || 'T' || turno.hora_inicio::time hora_inicio,
            cita.fecha || 'T' || turno.hora_final::time hora_final,
            SUM(CASE WHEN cita.estado = '1' THEN 1 ELSE 0 END) AS citas_libres,
            SUM(CASE WHEN cita.estado <> '1' THEN 1 ELSE 0 END) AS citas_ocupadas
        FROM cita
        INNER JOIN consultorio ON consultorio.id_consultorio=cita.id_consultorio
        INNER JOIN turno on turno.id_turno=cita.id_turno
        WHERE true
            and cita.fecha>='2022-12-26'
            and consultorio.id_especialidad='222400'
            and consultorio.id_estableciento='6184'
        GROUP BY 1,2,3,4, 5, 6
        '''
        data_list = cnx.execute(text(sql), id_estableciento=id_estableciento).fetchall()

    return render_template(
        'citas/nueva.html',
        ctx={
            'opcion': opcion,
            'constantes': constantes,
            'data_list': data_list,
        }
    )

@blueprint.route('/nueva/<fecha>/<int:id_turno>/<int:id_consultorio>', methods=['GET'])
@login_required
def asignar_cita(fecha, id_turno, id_consultorio):
    cnx = db.engine.connect()

    sql = '''
    SELECT id_cita from cita
    WHERE true
        and fecha=:fecha
        and id_turno=:id_turno
        and id_consultorio=:id_consultorio
        and estado='1'
        and id_paciente IS NULL
    ORDER BY hora_inicio
    LIMIT 1
    '''
    id_cita = cnx.execute(
        text(sql),
        fecha=fecha,
        id_turno=id_turno,
        id_consultorio=id_consultorio,
    ).fetchone()

    if id_cita:
        sql = '''
        UPDATE cita
            SET
                id_paciente=(
                    SELECT id_persona from paciente
                    WHERE usuario=:username
                    LIMIT 1
                ),
                estado='2'
        WHERE id_cita=:id_cita
        RETURNING id_cita;
        '''
        id_cita = cnx.execute(
            text(sql),
            username=current_user.username,
            id_cita=id_cita[0],
        ).fetchone()
        if id_cita:
            db.session.commit()
            print('>>>>> cita_id >>>>>', id_cita)
            return redirect(url_for('citas_blueprint.detalle_cita', id_cita=id_cita[0]))


@blueprint.route('/detalle/<int:id_cita>', methods=['GET'])
@login_required
def detalle_cita(id_cita):
    cnx = db.engine.connect()
    sql = '''
    SELECT
        persona.tipo_documento,
        persona.numero_documento,
        persona.apellido_paterno,
        persona.apellido_materno,
        persona.nombres,
        persona.fecha_nacimiento,
        persona.sexo,
        persona.email,
        persona.celular,
        persona.direccion,
        distrito.nombre distrito,
        cita.fecha cita_fecha,
        cita.hora_inicio,
        cita.hora_final
    FROM cita
    INNER JOIN persona ON persona.id_persona=cita.id_paciente
    INNER JOIN distrito on distrito.id_distrito=persona.id_distrito
    WHERE id_cita=:id_cita
    '''
    data = cnx.execute(text(sql), id_cita=id_cita).fetchone()

    return render_template(
        'citas/detalle.html',
        data=data,
    )
