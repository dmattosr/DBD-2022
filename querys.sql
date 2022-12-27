

DO $$
DECLARE
    row record;
    incremento int := 15;
    ttime time;
    ttime0 time;
    tfecha date;
    fecha_inicio date:= '2023-01-01';
    fecha_final date:= '2023-01-31';
BEGIN
    FOR row IN (
        SELECT
            turno.id_turno,
            turno.id_estableciento,
            consultorio.id_consultorio,
            turno.hora_inicio,
            turno.hora_final,
            medicoespecialidad.id_persona
        FROM turno
        INNER JOIN consultorio ON consultorio.id_estableciento=turno.id_estableciento
        INNER JOIN medicoespecialidad ON medicoespecialidad.id_especialidad=consultorio.id_especialidad
    )
    LOOP
        tfecha:=fecha_inicio;
        WHILE tfecha <= fecha_final LOOP
            ttime = row.hora_inicio::time;
            WHILE ttime < row.hora_final::time LOOP
                ttime0 = ttime;
                ttime = ttime + interval '1' MINUTE * (incremento);
                    INSERT INTO cita(
                        id_cita,
                        fecha,
                        hora_inicio,
                        hora_final,
                        estado,
                        tipo,
                        id_consultorio,
                        id_medico,
                        id_turno
                    ) VALUES (
                        nextval('cita__id_cita'),   -- id_cita
                        tfecha,                     -- fecha
                        ttime0,                     -- hora_inicio
                        ttime,                      -- hora_final
                        '1',                        -- estado
                        '1',                        -- tipo
                        row.id_consultorio,         -- id_consultorio
                        row.id_persona,             -- id_medico
                        row.id_turno                -- id_turno
                    );
            END LOOP;
            tfecha = tfecha + interval '1' DAY;
        END LOOP;
    END LOOP;
END$$;
