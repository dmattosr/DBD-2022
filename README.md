# DBD-2022


# Integrantes

- Aguirre Cardenas Patrick Bryan
- Mattos Rosales Daniel Alfredo
- Espinoza Ccente Miguel Ange
- Condori Mestas, Ledy Omar	

Querys
======


# Creacion de tablas


```sql

-- SECUENCIAS
CREATE SEQUENCE persona__id_persona
INCREMENT 1
START 1;


CREATE TABLE pais
(
  id_pais INT NOT NULL,
  nombre VARCHAR(30) NOT NULL,
  PRIMARY KEY (id_pais)
);

CREATE TABLE departamento
(
  id_departamento CHAR(2) NOT NULL,
  nombre VARCHAR(20) NOT NULL,
  PRIMARY KEY (id_departamento)
);

CREATE TABLE Provincia
(
  id_provincia CHAR(4) NOT NULL,
  nombre VARCHAR(30) NOT NULL,
  id_departamento CHAR(2) NOT NULL,
  PRIMARY KEY (id_provincia),
  FOREIGN KEY (id_departamento) REFERENCES departamento(id_departamento),
  UNIQUE (id_provincia, id_departamento)
);

CREATE TABLE Distrito
(
  id_distrito CHAR(6) NOT NULL,
  nombre VARCHAR(40) NOT NULL,
  id_provincia CHAR(4) NOT NULL,
  PRIMARY KEY (id_distrito),
  FOREIGN KEY (id_provincia) REFERENCES Provincia(id_provincia),
  UNIQUE (id_distrito, id_provincia)
);

CREATE TABLE Especialidad
(
  id_especialidad INT NOT NULL,
  nombre VARCHAR(100) NOT NULL,
  PRIMARY KEY (id_especialidad),
  UNIQUE (nombre)
);

CREATE TABLE Establecimiento
(
  id_estableciento CHAR(4) NOT NULL,
  nombre VARCHAR(100) NOT NULL,
  direccion VARCHAR(150) NOT NULL,
  latitud FLOAT NOT NULL,
  longitud FLOAT NOT NULL,
  altitud INT NOT NULL,
  telefono VARCHAR(9) NOT NULL,
  email VARCHAR(100) NOT NULL,
  nombre_director VARCHAR(100) NOT NULL,
  id_distrito CHAR(6) NOT NULL,
  PRIMARY KEY (id_estableciento),
  FOREIGN KEY (id_distrito) REFERENCES Distrito(id_distrito)
);


CREATE TABLE Turno
(
  id_turno INT NOT NULL,
  hora_inicio CHAR(8) NOT NULL,
  hora_final CHAR(8) NOT NULL,
  nombre VARCHAR(20) NOT NULL,
  id_estableciento CHAR(4) NOT NULL,
  PRIMARY KEY (id_turno),
  FOREIGN KEY (id_estableciento) REFERENCES Establecimiento(id_estableciento),
  UNIQUE (id_estableciento, hora_inicio, hora_final, nombre)
);

CREATE TABLE EstablecimientoEspecialidad
(
  id_estableciento CHAR(4) NOT NULL,
  id_especialidad INT NOT NULL,
  PRIMARY KEY (id_estableciento, id_especialidad),
  FOREIGN KEY (id_estableciento) REFERENCES Establecimiento(id_estableciento),
  FOREIGN KEY (id_especialidad) REFERENCES Especialidad(id_especialidad)
);



CREATE TABLE Persona
(
  id_persona INT NOT NULL,
  tipo_documento CHAR(2) NOT NULL, -- '01': DNI, '02': CARNET DE EXTRANJERIA
  numero_documento VARCHAR(9) NOT NULL,
  apellido_paterno VARCHAR(40) NOT NULL,
  apellido_materno VARCHAR(40) NOT NULL,
  nombres VARCHAR(40) NOT NULL,
  fecha_nacimiento DATE NOT NULL,
  sexo CHAR(2) NOT NULL, -- M: Masculino, F: Femenino
  email VARCHAR(150) NOT NULL,
  celular VARCHAR(9) NOT NULL,
  fecha_registro DATE NOT NULL,
  id_pais INT NOT NULL,
  id_distrito CHAR(6) NOT NULL,
  direccion VARCHAR(150) NOT NULL,
  PRIMARY KEY (id_persona),
  FOREIGN KEY (id_pais) REFERENCES pais(id_pais),
  FOREIGN KEY (id_distrito) REFERENCES Distrito(id_distrito)
);


CREATE TABLE Paciente
(
  id_persona INT NOT NULL,
  esta_activo INT NOT NULL,
  tipo_seguro CHAR(1) NOT NULL,
  usuario VARCHAR(20) NOT NULL,
  password VARCHAR(20) NOT NULL,
  PRIMARY KEY (id_persona),
  FOREIGN KEY (id_persona) REFERENCES Persona(id_persona)
);

CREATE TABLE Medico
(
  id_persona INT NOT NULL,
  esta_activo INT NOT NULL,
  num_colegiatura VARCHAR(15) NOT NULL,
  usuario VARCHAR(20) NOT NULL,
  password VARCHAR(40) NOT NULL,
  PRIMARY KEY (id_persona),
  FOREIGN KEY (id_persona) REFERENCES Persona(id_persona)
);


CREATE TABLE MedicoEspecialidad
(
  id_persona INT NOT NULL,
  id_especialidad INT NOT NULL,
  PRIMARY KEY (id_persona, id_especialidad),
  FOREIGN KEY (id_persona) REFERENCES Medico(id_persona),
  FOREIGN KEY (id_especialidad) REFERENCES Especialidad(id_especialidad)
);

CREATE TABLE Consultorio
(
  id_consultorio INT NOT NULL,
  nombre VARCHAR(50) NOT NULL,
  ubicacion VARCHAR(20) NOT NULL,
  id_estableciento CHAR(4) NOT NULL,
  id_especialidad INT NOT NULL,
  PRIMARY KEY (id_consultorio),
  FOREIGN KEY (id_especialidad) REFERENCES Especialidad(id_especialidad),
  FOREIGN KEY (id_estableciento) REFERENCES Establecimiento(id_estableciento),
  UNIQUE (id_especialidad, id_estableciento)
);


CREATE TABLE Cita
(
  id_cita INT NOT NULL,
  fecha DATE NOT NULL,
  hora_inicio CHAR(8) NOT NULL,
  hora_final CHAR(8) NOT NULL,
  estado INT NOT NULL,
  tipo CHAR(1) NOT NULL,
  calificacion_fecha INT,
  calificacion_puntaje INT,
  calificacion_comentario INT,
  diagnostico VARCHAR(1000),
  id_consultorio INT NOT NULL,
  id_paciente INT,
  id_medico INT NOT NULL,
  id_turno INT NOT NULL,
  PRIMARY KEY (id_cita),
  FOREIGN KEY (id_consultorio) REFERENCES Consultorio(id_consultorio),
  FOREIGN KEY (id_paciente) REFERENCES Paciente(id_persona),
  FOREIGN KEY (id_medico) REFERENCES Medico(id_persona),
  FOREIGN KEY (id_turno) REFERENCES Turno(id_turno)
);

```

# Poblamiento de tablas


```sql

INSERT INTO pais(id_pais, nombre) VALUES (1, 'PERU');
INSERT INTO pais(id_pais, nombre) VALUES (2, 'ARGENTINA');
INSERT INTO pais(id_pais, nombre) VALUES (3, 'BRASIL');
INSERT INTO pais(id_pais, nombre) VALUES (4, 'CHILE');
INSERT INTO pais(id_pais, nombre) VALUES (5, 'COLOMBIA');
INSERT INTO pais(id_pais, nombre) VALUES (10, 'VENEZUELA');



INSERT INTO departamento(id_departamento, nombre) VALUES ('01', 'AMAZONAS');
INSERT INTO departamento(id_departamento, nombre) VALUES ('02', 'ANCASH');
INSERT INTO departamento(id_departamento, nombre) VALUES ('03', 'APURIMAC');
INSERT INTO departamento(id_departamento, nombre) VALUES ('04', 'AREQUIPA');
INSERT INTO departamento(id_departamento, nombre) VALUES ('05', 'AYACUCHO');
INSERT INTO departamento(id_departamento, nombre) VALUES ('06', 'CAJAMARCA');
INSERT INTO departamento(id_departamento, nombre) VALUES ('07', 'CALLAO');
INSERT INTO departamento(id_departamento, nombre) VALUES ('08', 'CUSCO');
INSERT INTO departamento(id_departamento, nombre) VALUES ('09', 'HUANCAVELICA');
INSERT INTO departamento(id_departamento, nombre) VALUES ('10', 'HUANUCO');
INSERT INTO departamento(id_departamento, nombre) VALUES ('11', 'ICA');
INSERT INTO departamento(id_departamento, nombre) VALUES ('12', 'JUNIN');
INSERT INTO departamento(id_departamento, nombre) VALUES ('13', 'LA LIBERTAD');
INSERT INTO departamento(id_departamento, nombre) VALUES ('14', 'LAMBAYEQUE');
INSERT INTO departamento(id_departamento, nombre) VALUES ('15', 'LIMA');
INSERT INTO departamento(id_departamento, nombre) VALUES ('16', 'LORETO');
INSERT INTO departamento(id_departamento, nombre) VALUES ('17', 'MADRE DE DIOS');
INSERT INTO departamento(id_departamento, nombre) VALUES ('18', 'MOQUEGUA');
INSERT INTO departamento(id_departamento, nombre) VALUES ('19', 'PASCO');
INSERT INTO departamento(id_departamento, nombre) VALUES ('20', 'PIURA');
INSERT INTO departamento(id_departamento, nombre) VALUES ('21', 'PUNO');
INSERT INTO departamento(id_departamento, nombre) VALUES ('22', 'SAN MARTIN');
INSERT INTO departamento(id_departamento, nombre) VALUES ('23', 'TACNA');
INSERT INTO departamento(id_departamento, nombre) VALUES ('24', 'TUMBES');
INSERT INTO departamento(id_departamento, nombre) VALUES ('25', 'UCAYALI');




INSERT INTO provincia(id_departamento, id_provincia, nombre) VALUES ('15', '1501', 'LIMA');
INSERT INTO provincia(id_departamento, id_provincia, nombre) VALUES ('15', '1502', 'BARRANCA');
INSERT INTO provincia(id_departamento, id_provincia, nombre) VALUES ('15', '1503', 'CAJATAMBO');
INSERT INTO provincia(id_departamento, id_provincia, nombre) VALUES ('15', '1504', 'CANTA');
INSERT INTO provincia(id_departamento, id_provincia, nombre) VALUES ('15', '1505', 'CAÑETE');
INSERT INTO provincia(id_departamento, id_provincia, nombre) VALUES ('15', '1506', 'HUARAL');
INSERT INTO provincia(id_departamento, id_provincia, nombre) VALUES ('15', '1507', 'HUAROCHIRI');
INSERT INTO provincia(id_departamento, id_provincia, nombre) VALUES ('15', '1508', 'HUAURA');
INSERT INTO provincia(id_departamento, id_provincia, nombre) VALUES ('15', '1509', 'OYON');
INSERT INTO provincia(id_departamento, id_provincia, nombre) VALUES ('15', '1510', 'YAUYOS');

INSERT INTO distrito(id_provincia, id_distrito, nombre) VALUES ('1501', '150101', 'LIMA');
INSERT INTO distrito(id_provincia, id_distrito, nombre) VALUES ('1501', '150102', 'ANCON');
INSERT INTO distrito(id_provincia, id_distrito, nombre) VALUES ('1501', '150103', 'ATE');
INSERT INTO distrito(id_provincia, id_distrito, nombre) VALUES ('1501', '150105', 'BREÑA');
INSERT INTO distrito(id_provincia, id_distrito, nombre) VALUES ('1501', '150106', 'CARABAYLLO');
INSERT INTO distrito(id_provincia, id_distrito, nombre) VALUES ('1501', '150110', 'COMAS');
INSERT INTO distrito(id_provincia, id_distrito, nombre) VALUES ('1501', '150107', 'CHACLACAYO');
INSERT INTO distrito(id_provincia, id_distrito, nombre) VALUES ('1501', '150108', 'CHORRILLOS');
INSERT INTO distrito(id_provincia, id_distrito, nombre) VALUES ('1501', '150115', 'LA VICTORIA');
INSERT INTO distrito(id_provincia, id_distrito, nombre) VALUES ('1501', '150114', 'LA MOLINA');
INSERT INTO distrito(id_provincia, id_distrito, nombre) VALUES ('1501', '150116', 'LINCE');
INSERT INTO distrito(id_provincia, id_distrito, nombre) VALUES ('1501', '150118', 'LURIGANCHO');
INSERT INTO distrito(id_provincia, id_distrito, nombre) VALUES ('1501', '150119', 'LURIN');
INSERT INTO distrito(id_provincia, id_distrito, nombre) VALUES ('1501', '150120', 'MAGDALENA DEL MAR');
INSERT INTO distrito(id_provincia, id_distrito, nombre) VALUES ('1501', '150122', 'MIRAFLORES');
INSERT INTO distrito(id_provincia, id_distrito, nombre) VALUES ('1501', '150123', 'PACHACAMAC');
INSERT INTO distrito(id_provincia, id_distrito, nombre) VALUES ('1501', '150121', 'PUEBLO LIBRE');
INSERT INTO distrito(id_provincia, id_distrito, nombre) VALUES ('1501', '150124', 'PUCUSANA');
INSERT INTO distrito(id_provincia, id_distrito, nombre) VALUES ('1501', '150125', 'PUENTE PIEDRA');
INSERT INTO distrito(id_provincia, id_distrito, nombre) VALUES ('1501', '150126', 'PUNTA HERMOSA');
INSERT INTO distrito(id_provincia, id_distrito, nombre) VALUES ('1501', '150127', 'PUNTA NEGRA');
INSERT INTO distrito(id_provincia, id_distrito, nombre) VALUES ('1501', '150128', 'RIMAC');
INSERT INTO distrito(id_provincia, id_distrito, nombre) VALUES ('1501', '150129', 'SAN BARTOLO');
INSERT INTO distrito(id_provincia, id_distrito, nombre) VALUES ('1501', '150131', 'SAN ISIDRO');
INSERT INTO distrito(id_provincia, id_distrito, nombre) VALUES ('1501', '150104', 'BARRANCO');
INSERT INTO distrito(id_provincia, id_distrito, nombre) VALUES ('1501', '150135', 'SAN MARTIN DE PORRES');
INSERT INTO distrito(id_provincia, id_distrito, nombre) VALUES ('1501', '150136', 'SAN MIGUEL');
INSERT INTO distrito(id_provincia, id_distrito, nombre) VALUES ('1501', '150138', 'SANTA MARIA DEL MAR');
INSERT INTO distrito(id_provincia, id_distrito, nombre) VALUES ('1501', '150139', 'SANTA ROSA');
INSERT INTO distrito(id_provincia, id_distrito, nombre) VALUES ('1501', '150140', 'SANTIAGO DE SURCO');
INSERT INTO distrito(id_provincia, id_distrito, nombre) VALUES ('1501', '150141', 'SURQUILLO');
INSERT INTO distrito(id_provincia, id_distrito, nombre) VALUES ('1501', '150143', 'VILLA MARIA DEL TRIUNFO');
INSERT INTO distrito(id_provincia, id_distrito, nombre) VALUES ('1501', '150113', 'JESUS MARIA');
INSERT INTO distrito(id_provincia, id_distrito, nombre) VALUES ('1501', '150112', 'INDEPENDENCIA');
INSERT INTO distrito(id_provincia, id_distrito, nombre) VALUES ('1501', '150111', 'EL AGUSTINO');
INSERT INTO distrito(id_provincia, id_distrito, nombre) VALUES ('1501', '150133', 'SAN JUAN DE MIRAFLORES');
INSERT INTO distrito(id_provincia, id_distrito, nombre) VALUES ('1501', '150132', 'SAN JUAN DE LURIGANCHO');
INSERT INTO distrito(id_provincia, id_distrito, nombre) VALUES ('1501', '150134', 'SAN LUIS');
INSERT INTO distrito(id_provincia, id_distrito, nombre) VALUES ('1501', '150109', 'CIENEGUILLA');
INSERT INTO distrito(id_provincia, id_distrito, nombre) VALUES ('1501', '150130', 'SAN BORJA');
INSERT INTO distrito(id_provincia, id_distrito, nombre) VALUES ('1501', '150142', 'VILLA EL SALVADOR');
INSERT INTO distrito(id_provincia, id_distrito, nombre) VALUES ('1501', '150117', 'LOS OLIVOS');
INSERT INTO distrito(id_provincia, id_distrito, nombre) VALUES ('1501', '150137', 'SANTA ANITA');


INSERT INTO especialidad(id_especialidad, nombre) VALUES (222400, 'MEDICINA GENERAL');
INSERT INTO especialidad(id_especialidad, nombre) VALUES (221600, 'OBSTETRICIA');
INSERT INTO especialidad(id_especialidad, nombre) VALUES (220000, 'CRECIMIENTO Y DESARROLLO');
INSERT INTO especialidad(id_especialidad, nombre) VALUES (221900, 'ODONTOLOGIA');
INSERT INTO especialidad(id_especialidad, nombre) VALUES (200000, 'NUTRICION');
INSERT INTO especialidad(id_especialidad, nombre) VALUES (224102, 'PSICOLOGIA');
INSERT INTO especialidad(id_especialidad, nombre) VALUES (224700, 'PEDIATRIA');
INSERT INTO especialidad(id_especialidad, nombre) VALUES (221500, 'GINECOLOGIA');
INSERT INTO especialidad(id_especialidad, nombre) VALUES (260300, 'INMUNIZACIONES');
INSERT INTO especialidad(id_especialidad, nombre) VALUES (223400, 'TERAPIA FISICA Y REHABILITACION');
INSERT INTO especialidad(id_especialidad, nombre) VALUES (080400, 'DIAGNÓSTICO POR IMÁGENES -RADIODIAGNÓSTICO / RAYOS X');


INSERT INTO establecimiento(
  id_estableciento, nombre, direccion, latitud, longitud, altitud, telefono, email, nombre_director, id_distrito)
  VALUES
    ('6184', 'C.S. BREÑA', 'JR. NAPO 1445', -12.05691010, -77.05366011, 100, '4230432', 'csbreña@minsa.gob.pe','JOSE RAFAEL RAMIREZ', '150105'),
    ('6185', 'C.S. CHACRA COLORADA', 'JR. CARHUAZ 509', -12.05390390, -77.04811280, 100, '4231180', 'ccolorada@minsa.gob.pe','MARTIN REYES CAMPOS', '150105'),
    ('6186', 'C.S. CONDE DE LA VEGA Baja 3', 'JR. CONDE DE LA VEGA BAJA 488', -12.03815790, -77.05463250, 100, '3301547', 'emailAIL@minsa.gob.pe','MARIA SEGOBIA FARFAN', '150101'),
    ('6195', 'C.S. LINCE', 'JR. MANUEL CANDAMO 495', -12.08207950, -77.03186520, 100, '', 'email@minsa.gob.pe','MARIA RIVAS R.', '150116')
;

INSERT INTO turno(id_turno, id_estableciento, nombre, hora_inicio, hora_final) VALUES (1, '6184', 'MAÑANA', '08:00 AM', '01:00 PM');
INSERT INTO turno(id_turno, id_estableciento, nombre, hora_inicio, hora_final) VALUES (2, '6184', 'TARDE', '01:00 PM', '07:00 PM');
INSERT INTO turno(id_turno, id_estableciento, nombre, hora_inicio, hora_final) VALUES (3, '6185', 'MAÑANA', '08:00 AM', '01:00 PM');
INSERT INTO turno(id_turno, id_estableciento, nombre, hora_inicio, hora_final) VALUES (4, '6185', 'TARDE', '01:00 PM', '07:00 PM');
INSERT INTO turno(id_turno, id_estableciento, nombre, hora_inicio, hora_final) VALUES (5, '6186', 'MAÑANA', '08:00 AM', '01:00 PM');
INSERT INTO turno(id_turno, id_estableciento, nombre, hora_inicio, hora_final) VALUES (6, '6186', 'TARDE', '01:00 PM', '07:00 PM');
INSERT INTO turno(id_turno, id_estableciento, nombre, hora_inicio, hora_final) VALUES (7, '6195', 'MAÑANA', '08:00 AM', '01:00 PM');
INSERT INTO turno(id_turno, id_estableciento, nombre, hora_inicio, hora_final) VALUES (8, '6195', 'TARDE', '01:00 PM', '07:00 PM');



INSERT INTO EstablecimientoEspecialidad(id_estableciento, id_especialidad) VALUES
  ('6184',222400),
  ('6184',221600),
  ('6184',220000),
  ('6184',221900),
  ('6184',200000),
  ('6184',224102),
  ('6184',224700),
  ('6184',221500),
  ('6184',260300)
;

INSERT INTO EstablecimientoEspecialidad(id_estableciento, id_especialidad) VALUES
  ('6195',222400),
  ('6195',221600),
  ('6195',220000),
  ('6195',221900),
  ('6195',200000),
  ('6195',224102),
  ('6195',224700),
  ('6195',221500),
  ('6195',260300),
  ('6195',223400),
  ('6195',080400)
;

INSERT INTO EstablecimientoEspecialidad(id_estableciento, id_especialidad) VALUES
  ('6185',222400),
  ('6185',221900),
  ('6185',224102),
  ('6185',224700),
  ('6185',221500)
;

INSERT INTO EstablecimientoEspecialidad(id_estableciento, id_especialidad) VALUES
  ('6186',222400),
  ('6186',221900),
  ('6186',224102),
  ('6186',224700),
  ('6186',221500)
;



INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (1, '01', 12288572, 'Capin', 'Julian', 'Stanwood', '1989-05-19', 'M', 'sjulian0@dagondesign.com', '90338415', '1985-11-06', 1, '150101', '43 Blaine Place');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (2, '01', 18251683, 'Aingell', 'Mingasson', 'Milicent', '1981-09-19', 'F', 'mmingasson1@scribd.com', '92115593', '1989-01-04', 1, '150112', '211 Lawn Circle');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (3, '01', 53864503, 'Hacksby', 'Towriss', 'Sigfrid', '1998-01-27', 'M', 'stowriss2@scribd.com', '91435444', '1994-05-13', 1, '150106', '6 Daystar Street');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (4, '01', 45352090, 'Moyser', 'Brendeke', 'Bondie', '1984-07-10', 'M', 'bbrendeke3@xrea.com', '99222766', '1999-11-09', 1, '150101', '6361 Hollow Ridge Street');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (5, '01', 50040305, 'Fitch', 'Dunguy', 'King', '1995-06-09', 'M', 'kdunguy4@ucoz.com', '97825016', '1983-08-12', 1, '150105', '78411 Russell Avenue');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (6, '01', 31681877, 'Bradwell', 'Hutchison', 'Martina', '1984-11-04', 'F', 'mhutchison5@shinystat.com', '99599243', '1991-10-10', 1, '150101', '3645 Donald Trail');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (7, '01', 55000159, 'Antognazzi', 'Adame', 'Jard', '1985-07-22', 'M', 'jadame6@shutterfly.com', '99559626', '1999-11-25', 1, '150101', '3 Elka Avenue');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (8, '01', 16727371, 'Hiorn', 'Wimpress', 'Bryna', '1994-10-01', 'F', 'bwimpress7@bandcamp.com', '90383144', '1980-11-17', 1, '150128', '6376 Haas Road');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (9, '01', 23087675, 'Halfhead', 'Botcherby', 'Fidel', '1994-02-25', 'M', 'fbotcherby8@icio.us', '94912874', '1986-08-25', 1, '150113', '52591 Gina Court');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (10, '01', 26491811, 'Phillpot', 'Issard', 'Angelita', '1999-05-13', 'F', 'aissard9@wordpress.org', '90792088', '1999-01-17', 1, '150101', '31430 Debra Trail');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (11, '01', 19366079, 'Kemble', 'Solland', 'Ermanno', '1985-07-28', 'M', 'esollanda@nifty.com', '97714644', '1988-03-09', 1, '150101', '50955 Elgar Hill');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (12, '01', 44311308, 'Bimrose', 'Lailey', 'Dill', '1998-09-28', 'M', 'dlaileyb@facebook.com', '96406314', '1996-01-17', 1, '150116', '94693 Susan Point');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (13, '01', 21067934, 'Coudray', 'Ilden', 'Conrad', '2000-06-04', 'M', 'cildenc@amazonaws.com', '94405641', '1997-03-02', 1, '150101', '557 Emmet Pass');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (14, '01', 69766864, 'Trouel', 'Mallen', 'Corbet', '1997-10-09', 'M', 'cmallend@walmart.com', '96539685', '1998-07-06', 1, '150120', '544 Morningstar Pass');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (15, '01', 61370181, 'Fardy', 'Doghartie', 'Natal', '1990-01-15', 'M', 'ndoghartiee@businesswire.com', '99938631', '1999-10-01', 1, '150142', '58 Vernon Alley');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (16, '01', 28146137, 'Kerbey', 'Plant', 'Pauly', '1983-08-18', 'F', 'pplantf@posterous.com', '91139391', '1985-06-16', 1, '150142', '7 Bunker Hill Trail');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (17, '01', 23991918, 'Rodgers', 'Bentick', 'Fianna', '1984-04-18', 'F', 'fbentickg@google.com.au', '96798074', '1997-05-21', 1, '150119', '3 Thackeray Crossing');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (18, '01', 69657142, 'Cashford', 'Mish', 'Shadow', '1994-12-07', 'M', 'smishh@telegraph.co.uk', '94954711', '1981-10-07', 1, '150140', '97883 Weeping Birch Pass');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (19, '01', 50597524, 'Benesevich', 'Weems', 'Virginia', '1997-08-21', 'F', 'vweemsi@fc2.com', '94784200', '1994-08-17', 1, '150101', '2873 Pierstorff Road');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (20, '01', 29377459, 'Louiset', 'Sirey', 'Brigham', '1986-02-19', 'M', 'bsireyj@is.gd', '99647345', '1992-07-17', 1, '150119', '3 Judy Hill');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (21, '01', 29603833, 'McKinnell', 'Rickaert', 'Terese', '1989-03-18', 'F', 'trickaertk@msn.com', '90670396', '1987-01-02', 1, '150119', '9 Anzinger Drive');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (22, '01', 28245339, 'Kell', 'Edler', 'Jyoti', '1997-04-22', 'F', 'jedlerl@about.com', '92542903', '1998-06-25', 1, '150101', '323 Merchant Hill');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (23, '01', 25724008, 'Jeremaes', 'Treker', 'Hetty', '1988-10-21', 'F', 'htrekerm@rediff.com', '93113728', '1982-07-23', 1, '150119', '33188 Harper Plaza');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (24, '01', 22193302, 'Hrishchenko', 'Gannan', 'Townsend', '1982-08-03', 'M', 'tgannann@narod.ru', '98935245', '1990-05-09', 1, '150119', '890 Messerschmidt Lane');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (25, '01', 12915091, 'Rickardes', 'Hansberry', 'Manolo', '1998-02-11', 'M', 'mhansberryo@bravesites.com', '95259142', '1987-01-16', 1, '150112', '2412 Waywood Parkway');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (26, '01', 19835590, 'Moakler', 'Pavy', 'Katy', '1996-09-10', 'F', 'kpavyp@cdc.gov', '93922601', '1989-12-25', 1, '150107', '41 Homewood Point');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (27, '01', 48535024, 'MacLese', 'Martello', 'Quill', '1986-07-27', 'M', 'qmartelloq@zimbio.com', '92950888', '1991-04-13', 1, '150139', '40 Mallory Court');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (28, '01', 63425169, 'Kettley', 'McGilleghole', 'Bell', '1986-01-28', 'F', 'bmcgillegholer@indiegogo.com', '90501899', '1986-02-04', 1, '150143', '8749 Scofield Plaza');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (29, '01', 54134814, 'Keymar', 'Bevan', 'Nobe', '1993-09-03', 'M', 'nbevans@sun.com', '98783013', '1990-08-31', 1, '150141', '3524 Arizona Pass');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (30, '01', 37356208, 'Herreran', 'Foltin', 'Livvyy', '1999-05-24', 'F', 'lfoltint@mlb.com', '99353984', '1990-10-28', 1, '150139', '9320 Kipling Way');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (31, '01', 54632221, 'McNellis', 'Fatkin', 'Mary', '1985-05-09', 'F', 'mfatkinu@aol.com', '95904271', '1985-02-12', 1, '150101', '9543 Warbler Place');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (32, '01', 45117793, 'Anstey', 'Lanyon', 'Doralynne', '1992-09-17', 'F', 'dlanyonv@umn.edu', '99164308', '1982-02-26', 1, '150139', '18 Towne Alley');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (33, '01', 62584907, 'Wormstone', 'Cartman', 'Delmor', '1988-04-09', 'M', 'dcartmanw@domainmarket.com', '97513294', '1999-04-15', 1, '150139', '357 Park Meadow Court');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (34, '01', 61981838, 'Varga', 'Gartland', 'Mandy', '1999-04-13', 'F', 'mgartlandx@imdb.com', '90246678', '1982-04-11', 1, '150139', '168 Hansons Point');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (35, '01', 60352439, 'Ure', 'Norfolk', 'Weber', '1997-01-02', 'M', 'wnorfolky@about.com', '91830312', '1981-03-16', 1, '150116', '67 Columbus Hill');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (36, '01', 30285257, 'De Atta', 'Loughney', 'Archibold', '1995-03-21', 'M', 'aloughneyz@ihg.com', '96241216', '1985-03-14', 1, '150139', '275 Twin Pines Crossing');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (37, '01', 21230331, 'Cusiter', 'Helliar', 'Marlo', '1986-07-05', 'M', 'mhelliar10@t.co', '94429369', '1993-02-21', 1, '150139', '0 Rutledge Terrace');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (38, '01', 66620971, 'Lidell', 'Bramham', 'Sam', '1982-07-07', 'M', 'sbramham11@prnewswire.com', '98303515', '1995-01-09', 1, '150141', '8 Texas Terrace');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (39, '01', 20060642, 'Pawlik', 'Schofield', 'Amity', '1991-12-17', 'F', 'aschofield12@amazon.co.jp', '97930698', '1982-12-28', 1, '150141', '7387 Hermina Junction');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (40, '01', 46385768, 'Burnall', 'Gelder', 'Clio', '1986-08-09', 'F', 'cgelder13@mozilla.org', '91682225', '1997-04-27', 1, '150141', '847 Garrison Park');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (41, '01', 43894974, 'Hallick', 'Fairclough', 'Berny', '1987-03-05', 'M', 'bfairclough14@indiatimes.com', '97302314', '1982-12-31', 1, '150126', '70882 Reindahl Hill');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (42, '01', 12852652, 'Raoul', 'Chatten', 'Sidonia', '1991-04-10', 'F', 'schatten15@delicious.com', '96222893', '1982-09-17', 1, '150143', '8 Washington Lane');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (43, '01', 62249614, 'Ebbitt', 'Christley', 'Toinette', '1984-05-02', 'F', 'tchristley16@wikispaces.com', '96237667', '1993-09-28', 1, '150143', '8725 Sunbrook Drive');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (44, '01', 44224869, 'Ansell', 'Adamowicz', 'Nobie', '1991-04-17', 'M', 'nadamowicz17@google.com.au', '93810254', '1998-07-27', 1, '150101', '49 Marquette Hill');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (45, '01', 14838388, 'Huntall', 'Dubose', 'Terence', '1991-08-03', 'M', 'tdubose18@bloglovin.com', '90734977', '1992-05-26', 1, '150101', '3 6th Drive');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (46, '01', 17668767, 'Barthrup', 'Trivett', 'Ellery', '1986-09-24', 'M', 'etrivett19@va.gov', '90626365', '1995-01-30', 1, '150101', '41 Lake View Road');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (47, '01', 16141526, 'Applewhaite', 'Harnor', 'Val', '1999-10-14', 'M', 'vharnor1a@stanford.edu', '91464202', '1992-08-15', 1, '150123', '26 Mosinee Road');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (48, '01', 30952096, 'Driscoll', 'Roumier', 'Rozanne', '1990-12-14', 'F', 'rroumier1b@wordpress.com', '92012858', '1997-04-04', 1, '150101', '1994 Karstens Crossing');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (49, '01', 18584886, 'Aulds', 'Simonutti', 'Odie', '1990-12-21', 'M', 'osimonutti1c@vimeo.com', '92404467', '1999-08-26', 1, '150101', '82 Packers Parkway');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (50, '01', 46341499, 'Capstick', 'Mandy', 'Tybi', '1988-03-24', 'F', 'tmandy1d@yahoo.com', '95184019', '1988-09-25', 1, '150140', '2293 Cardinal Road');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (51, '01', 47570259, 'Cawt', 'Fearnill', 'Freddy', '1996-04-21', 'M', 'ffearnill1e@msn.com', '98862619', '1989-02-11', 1, '150140', '3 Melvin Point');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (52, '01', 60790947, 'McLae', 'Hattam', 'Zack', '1993-08-28', 'M', 'zhattam1f@mozilla.com', '99538521', '1995-02-25', 1, '150140', '11 Monterey Terrace');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (53, '01', 31993547, 'Shipston', 'Jalland', 'Catarina', '1989-02-18', 'F', 'cjalland1g@rakuten.co.jp', '97898689', '1986-04-03', 1, '150105', '14352 Surrey Parkway');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (54, '01', 53089520, 'Mendez', 'Shellard', 'Fredric', '1991-01-09', 'M', 'fshellard1h@macromedia.com', '94449510', '1990-03-28', 1, '150140', '238 Norway Maple Drive');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (55, '01', 52122761, 'Barnwill', 'Crannis', 'Brnaba', '1999-08-14', 'M', 'bcrannis1i@mlb.com', '94794816', '1985-06-14', 1, '150101', '1805 Charing Cross Terrace');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (56, '01', 31188080, 'Roby', 'Probat', 'Monro', '1999-10-28', 'M', 'mprobat1j@google.ru', '98872373', '1984-01-03', 1, '150140', '277 Eggendart Pass');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (57, '01', 39971417, 'Woltman', 'Verrills', 'Cthrine', '1985-10-19', 'F', 'cverrills1k@clickbank.net', '91286134', '1996-07-22', 1, '150140', '935 Oriole Pass');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (58, '01', 10198084, 'Kulicke', 'Fowell', 'Roberto', '1983-11-25', 'M', 'rfowell1l@miitbeian.gov.cn', '94029537', '1990-04-03', 1, '150101', '38785 Monument Way');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (59, '01', 48966320, 'Mynett', 'Robjohns', 'Hallie', '1983-03-13', 'F', 'hrobjohns1m@paypal.com', '90664224', '1999-06-11', 1, '150103', '9985 Stephen Avenue');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (60, '01', 12868737, 'Menendes', 'Lowrey', 'Korey', '1983-06-15', 'M', 'klowrey1n@yolasite.com', '91949160', '1991-10-26', 1, '150140', '16 Prentice Drive');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (61, '01', 18454275, 'Krochmann', 'Richfield', 'Maris', '1989-07-03', 'F', 'mrichfield1o@ucoz.com', '93263113', '1984-08-23', 1, '150119', '62584 High Crossing Road');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (62, '01', 9508068, 'Paulich', 'Pennycook', 'Renie', '1998-08-27', 'F', 'rpennycook1p@state.gov', '97892958', '1986-11-24', 1, '150140', '851 Red Cloud Pass');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (63, '01', 30777481, 'Woolland', 'Polotti', 'Son', '1988-06-14', 'M', 'spolotti1q@tiny.cc', '99564158', '1986-08-26', 1, '150104', '7691 Heffernan Road');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (64, '01', 39577447, 'Lifton', 'Arnatt', 'Marylou', '1986-12-29', 'F', 'marnatt1r@businessinsider.com', '91436460', '1987-09-18', 1, '150141', '24 Anniversary Alley');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (65, '01', 16649742, 'Laffin', 'Tidmas', 'Henryetta', '1988-05-20', 'F', 'htidmas1s@oaic.gov.au', '90443242', '1988-08-24', 1, '150140', '505 Knutson Pass');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (66, '01', 38770831, 'Tamas', 'Le Galle', 'Josi', '2000-08-01', 'F', 'jlegalle1t@walmart.com', '96752843', '1980-11-08', 1, '150106', '3300 Delaware Avenue');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (67, '01', 33799214, 'Morforth', 'Davidsson', 'Bamby', '1998-03-10', 'F', 'bdavidsson1u@so-net.ne.jp', '94864687', '1999-08-30', 1, '150140', '0612 Mallard Street');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (68, '01', 19282924, 'Loud', 'Rosenau', 'Eduardo', '1993-07-18', 'M', 'erosenau1v@tripod.com', '91366271', '1994-06-09', 1, '150118', '0439 Jenna Pass');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (69, '01', 47221471, 'Bird', 'Eliyahu', 'Gerardo', '1999-09-13', 'M', 'geliyahu1w@nasa.gov', '97071676', '1992-02-09', 1, '150140', '46 Corscot Plaza');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (70, '01', 23857767, 'Bridgeland', 'Emby', 'Georgi', '1995-10-30', 'M', 'gemby1x@ca.gov', '96872654', '1999-11-22', 1, '150140', '70884 Luster Avenue');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (71, '01', 53634828, 'Harragin', 'Huitt', 'Alysa', '1996-05-19', 'F', 'ahuitt1y@mapquest.com', '90805461', '1991-04-12', 1, '150143', '94700 Buell Circle');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (72, '01', 33825530, 'Gehrels', 'Bengochea', 'Cy', '2000-08-01', 'M', 'cbengochea1z@usda.gov', '92635436', '1998-04-04', 1, '150131', '9730 Washington Parkway');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (73, '01', 41843715, 'Campione', 'Paute', 'Robin', '1988-11-03', 'F', 'rpaute20@whitehouse.gov', '98071863', '1998-12-18', 1, '150131', '99598 Walton Drive');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (74, '01', 38527399, 'Cant', 'Vickar', 'Finn', '1990-09-17', 'M', 'fvickar21@wordpress.com', '93973413', '1985-05-19', 1, '150104', '923 Thompson Center');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (75, '01', 42132636, 'Shevell', 'Seabrocke', 'Dyanne', '1984-08-31', 'F', 'dseabrocke22@craigslist.org', '96090516', '1987-01-14', 1, '150140', '68 Kim Lane');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (76, '01', 24292511, 'Dodgson', 'Bayless', 'Lauritz', '1989-05-04', 'M', 'lbayless23@go.com', '90964666', '1982-09-25', 1, '150104', '050 Becker Point');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (77, '01', 24918135, 'Defty', 'Moakson', 'Alleen', '1981-09-15', 'F', 'amoakson24@studiopress.com', '97661607', '1997-03-01', 1, '150110', '4277 Granby Hill');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (78, '01', 54505189, 'Durtnal', 'Lacotte', 'Kendal', '1997-10-10', 'M', 'klacotte25@sciencedirect.com', '92244899', '1985-03-05', 1, '150140', '731 Dryden Road');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (79, '01', 41786297, 'Brazel', 'Hulbert', 'Shirl', '1981-08-28', 'F', 'shulbert26@reddit.com', '96789628', '1992-05-12', 1, '150140', '6586 Crescent Oaks Parkway');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (80, '01', 68296535, 'Paolo', 'Martignon', 'Osbert', '1991-08-25', 'M', 'omartignon27@ca.gov', '91071081', '1994-09-02', 1, '150101', '8 Grayhawk Way');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (81, '01', 57266054, 'Heath', 'Monnoyer', 'Dayle', '1989-01-15', 'F', 'dmonnoyer28@go.com', '99486726', '1997-11-30', 1, '150101', '71 Parkside Park');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (82, '01', 66899329, 'Teers', 'Chasle', 'Rubie', '1987-10-19', 'F', 'rchasle29@hatena.ne.jp', '99719747', '1991-01-15', 1, '150103', '955 Ridgeview Parkway');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (83, '01', 43684900, 'Andrioni', 'Esberger', 'Giulietta', '1988-03-29', 'F', 'gesberger2a@nih.gov', '97237586', '1981-04-07', 1, '150143', '3 Bartelt Avenue');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (84, '01', 64044032, 'Badcock', 'Pepler', 'Dedra', '1985-12-28', 'F', 'dpepler2b@miibeian.gov.cn', '98697775', '1999-03-16', 1, '150143', '43458 Brickson Park Park');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (85, '01', 15628542, 'Slimings', 'Wood', 'Kort', '1992-02-13', 'M', 'kwood2c@w3.org', '92701663', '1993-11-20', 1, '150143', '374 Hanson Park');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (86, '01', 20263659, 'Laydel', 'Swinden', 'Onfroi', '1991-10-19', 'M', 'oswinden2d@goo.gl', '94542206', '1992-12-25', 1, '150101', '802 Sutherland Trail');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (87, '01', 50930643, 'Olivi', 'Woolaghan', 'Edan', '1991-01-26', 'M', 'ewoolaghan2e@oaic.gov.au', '95529819', '1998-06-06', 1, '150101', '374 Calypso Point');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (88, '01', 26455127, 'Frayling', 'Umfrey', 'Stevie', '1986-10-06', 'M', 'sumfrey2f@blogger.com', '94863002', '1991-12-08', 1, '150101', '135 Kim Court');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (89, '01', 15643545, 'Liddell', 'Ritchman', 'Ronnie', '1984-10-13', 'F', 'rritchman2g@tinyurl.com', '97228891', '1984-09-24', 1, '150113', '135 Cardinal Point');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (90, '01', 54162360, 'Jelks', 'Shovelbottom', 'Kathlin', '1995-12-17', 'F', 'kshovelbottom2h@wikimedia.org', '91450868', '1989-03-18', 1, '150127', '9642 Armistice Drive');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (91, '01', 32566382, 'Overel', 'Costelow', 'Kaitlynn', '1988-11-23', 'F', 'kcostelow2i@uiuc.edu', '92576468', '1981-02-26', 1, '150107', '2 Miller Way');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (92, '01', 28220172, 'Derisley', 'Longina', 'Dena', '1982-04-02', 'F', 'dlongina2j@usgs.gov', '98642889', '1985-02-12', 1, '150101', '607 Hintze Pass');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (93, '01', 21440305, 'Tewkesberry', 'Louedey', 'Roch', '1996-01-28', 'F', 'rlouedey2k@netlog.com', '94400195', '1982-03-18', 1, '150101', '66417 Dryden Crossing');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (94, '01', 66727398, 'Rapinett', 'Bonnesen', 'Datha', '1994-02-22', 'F', 'dbonnesen2l@sciencedirect.com', '98159981', '1985-08-03', 1, '150103', '7634 Brown Terrace');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (95, '01', 67732930, 'Logsdail', 'Tyas', 'Trever', '1984-02-12', 'M', 'ttyas2m@techcrunch.com', '98960411', '1991-02-07', 1, '150101', '5 Rusk Place');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (96, '01', 9010736, 'Orgel', 'Wignall', 'Georgette', '1984-01-05', 'F', 'gwignall2n@google.de', '96624761', '1988-07-04', 1, '150113', '060 Onsgard Drive');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (97, '01', 54324937, 'Gammidge', 'Durden', 'Cody', '1986-02-25', 'F', 'cdurden2o@cornell.edu', '93786519', '1988-07-26', 1, '150143', '996 Anzinger Terrace');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (98, '01', 66104069, 'Glason', 'Dewicke', 'Milton', '1994-04-21', 'M', 'mdewicke2p@hatena.ne.jp', '97097614', '1982-10-13', 1, '150101', '9864 Dapin Point');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (99, '01', 29093256, 'Crosthwaite', 'Skellorne', 'Alvy', '1995-11-24', 'M', 'askellorne2q@deliciousdays.com', '97877106', '1992-07-29', 1, '150101', '024 Memorial Junction');
INSERT INTO persona (id_persona, tipo_documento, numero_documento, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, sexo, email, celular, fecha_registro, id_pais, id_distrito, direccion) VALUES (100, '01', 52942639, 'Tureville', 'Tillard', 'Lelia', '2000-08-11', 'F', 'ltillard2r@shop-pro.jp', '96444736', '1995-02-12', 1, '150101', '70 Superior Plaza');







insert into paciente (id_persona, esta_activo, tipo_seguro, usuario, password) values (49, 1, '1', 'vcaulfield0', '12345678');
insert into paciente (id_persona, esta_activo, tipo_seguro, usuario, password) values (89, 1, '1', 'slunney1', '12345678');
insert into paciente (id_persona, esta_activo, tipo_seguro, usuario, password) values (16, 1, '1', 'aaylmore2', '12345678');
insert into paciente (id_persona, esta_activo, tipo_seguro, usuario, password) values (7, 1, '1', 'oscoyne3', '12345678');
insert into paciente (id_persona, esta_activo, tipo_seguro, usuario, password) values (73, 1, '1', 'swyldes4', '12345678');
insert into paciente (id_persona, esta_activo, tipo_seguro, usuario, password) values (30, 1, '1', 'skadwallider5', '12345678');
insert into paciente (id_persona, esta_activo, tipo_seguro, usuario, password) values (23, 1, '1', 'vborman6', '12345678');
insert into paciente (id_persona, esta_activo, tipo_seguro, usuario, password) values (100, 1, '1', 'spurslow7', '12345678');
insert into paciente (id_persona, esta_activo, tipo_seguro, usuario, password) values (12, 1, '1', 'eseiller8', '12345678');
insert into paciente (id_persona, esta_activo, tipo_seguro, usuario, password) values (95, 1, '1', 'amcilmorow9', '12345678');
insert into paciente (id_persona, esta_activo, tipo_seguro, usuario, password) values (65, 1, '1', 'fhaiga', '12345678');
insert into paciente (id_persona, esta_activo, tipo_seguro, usuario, password) values (64, 1, '1', 'ndobrowskib', '12345678');
insert into paciente (id_persona, esta_activo, tipo_seguro, usuario, password) values (83, 1, '1', 'bgreevesonc', '12345678');
insert into paciente (id_persona, esta_activo, tipo_seguro, usuario, password) values (2, 1, '1', 'dhatchardd', '12345678');
insert into paciente (id_persona, esta_activo, tipo_seguro, usuario, password) values (3, 1, '1', 'rsellorse', '12345678');
insert into paciente (id_persona, esta_activo, tipo_seguro, usuario, password) values (99, 1, '1', 'vemeryf', '12345678');
insert into paciente (id_persona, esta_activo, tipo_seguro, usuario, password) values (4, 1, '1', 'ocookeg', '12345678');
insert into paciente (id_persona, esta_activo, tipo_seguro, usuario, password) values (72, 1, '1', 'lellioth', '12345678');
insert into paciente (id_persona, esta_activo, tipo_seguro, usuario, password) values (77, 1, '1', 'gwynei', '12345678');
insert into paciente (id_persona, esta_activo, tipo_seguro, usuario, password) values (82, 1, '1', 'ablaskettj', '12345678');
insert into paciente (id_persona, esta_activo, tipo_seguro, usuario, password) values (54, 1, '1', 'rmedlerk', '12345678');
insert into paciente (id_persona, esta_activo, tipo_seguro, usuario, password) values (88, 1, '1', 'babelll', '12345678');
insert into paciente (id_persona, esta_activo, tipo_seguro, usuario, password) values (28, 1, '1', 'seccleshallm', '12345678');
insert into paciente (id_persona, esta_activo, tipo_seguro, usuario, password) values (8, 1, '1', 'telwynn', '12345678');
insert into paciente (id_persona, esta_activo, tipo_seguro, usuario, password) values (40, 1, '1', 'ggillbeyo', '12345678');
insert into paciente (id_persona, esta_activo, tipo_seguro, usuario, password) values (63, 1, '1', 'mrollinsonp', '12345678');
insert into paciente (id_persona, esta_activo, tipo_seguro, usuario, password) values (81, 1, '1', 'dhalledeq', '12345678');
insert into paciente (id_persona, esta_activo, tipo_seguro, usuario, password) values (74, 1, '1', 'ntallonr', '12345678');
insert into paciente (id_persona, esta_activo, tipo_seguro, usuario, password) values (33, 1, '1', 'ipurkisss', '12345678');
insert into paciente (id_persona, esta_activo, tipo_seguro, usuario, password) values (59, 1, '1', 'hmcilwratht', '12345678');




insert into medico (id_persona, esta_activo, num_colegiatura, usuario, password) values (99, 1, '99991114', 'cbrumhead0', '12345678');
insert into medico (id_persona, esta_activo, num_colegiatura, usuario, password) values (13, 1, '99998234', 'heakly1', '12345678');
insert into medico (id_persona, esta_activo, num_colegiatura, usuario, password) values (60, 1, '99992221', 'blung2', '12345678');
insert into medico (id_persona, esta_activo, num_colegiatura, usuario, password) values (11, 1, '99992119', 'sfyrth3', '12345678');
insert into medico (id_persona, esta_activo, num_colegiatura, usuario, password) values (14, 1, '99998970', 'jsykora4', '12345678');
insert into medico (id_persona, esta_activo, num_colegiatura, usuario, password) values (30, 1, '99997828', 'dmanby5', '12345678');
insert into medico (id_persona, esta_activo, num_colegiatura, usuario, password) values (5, 1, '99997284', 'cmanger6', '12345678');
insert into medico (id_persona, esta_activo, num_colegiatura, usuario, password) values (35, 1, '99991782', 'cceller7', '12345678');
insert into medico (id_persona, esta_activo, num_colegiatura, usuario, password) values (25, 1, '99994138', 'rwearn8', '12345678');
insert into medico (id_persona, esta_activo, num_colegiatura, usuario, password) values (67, 1, '99993173', 'malhirsi9', '12345678');
insert into medico (id_persona, esta_activo, num_colegiatura, usuario, password) values (80, 1, '99998690', 'atobya', '12345678');
insert into medico (id_persona, esta_activo, num_colegiatura, usuario, password) values (51, 1, '99997175', 'dhupeb', '12345678');
insert into medico (id_persona, esta_activo, num_colegiatura, usuario, password) values (87, 1, '99995510', 'dklimmekc', '12345678');
insert into medico (id_persona, esta_activo, num_colegiatura, usuario, password) values (94, 1, '99993769', 'mtremained', '12345678');
insert into medico (id_persona, esta_activo, num_colegiatura, usuario, password) values (55, 1, '99996185', 'llequeuxe', '12345678');


insert into medicoespecialidad (id_persona, id_especialidad) values (99, 224700);
insert into medicoespecialidad (id_persona, id_especialidad) values (99, 221600);
insert into medicoespecialidad (id_persona, id_especialidad) values (13, 222400);
insert into medicoespecialidad (id_persona, id_especialidad) values (60, 200000);
insert into medicoespecialidad (id_persona, id_especialidad) values (11, 224700);
insert into medicoespecialidad (id_persona, id_especialidad) values (14, 221500);
insert into medicoespecialidad (id_persona, id_especialidad) values (30, 222400);
insert into medicoespecialidad (id_persona, id_especialidad) values (5, 221500);
insert into medicoespecialidad (id_persona, id_especialidad) values (35, 222400);
insert into medicoespecialidad (id_persona, id_especialidad) values (25, 224700);
insert into medicoespecialidad (id_persona, id_especialidad) values (67, 221500);
insert into medicoespecialidad (id_persona, id_especialidad) values (80, 222400);
insert into medicoespecialidad (id_persona, id_especialidad) values (51, 222400);
insert into medicoespecialidad (id_persona, id_especialidad) values (87, 200000);
insert into medicoespecialidad (id_persona, id_especialidad) values (94, 222400);
insert into medicoespecialidad (id_persona, id_especialidad) values (55, 221600);



insert INTO consultorio (id_consultorio, id_estableciento, id_especialidad, nombre, ubicacion) VALUES (1, '6184', 222400, 'MEDICINA 01', 'CONSULTORIO 01');
insert INTO consultorio (id_consultorio, id_estableciento, id_especialidad, nombre, ubicacion) VALUES (2, '6185', 222400, 'MEDICINA 01', 'CONSULTORIO 01');
insert INTO consultorio (id_consultorio, id_estableciento, id_especialidad, nombre, ubicacion) VALUES (3, '6186', 222400, 'MEDICINA 01', 'CONSULTORIO 01');
insert INTO consultorio (id_consultorio, id_estableciento, id_especialidad, nombre, ubicacion) VALUES (4, '6195', 222400, 'MEDICINA 01', 'CONSULTORIO 01');




INSERT INTO cita(id_cita, fecha, hora_inicio, hora_final, estado, tipo, id_consultorio, id_medico, id_turno) VALUES (1, '2022-01-01', '08:00 AM', '08:20 AM', 1, '1', 1, 99, 1);
INSERT INTO cita(id_cita, fecha, hora_inicio, hora_final, estado, tipo, id_consultorio, id_medico, id_turno) VALUES (2, '2022-01-01', '08:20 AM', '08:40 AM', 1, '1', 1, 99, 1);
INSERT INTO cita(id_cita, fecha, hora_inicio, hora_final, estado, tipo, id_consultorio, id_medico, id_turno) VALUES (3, '2022-01-01', '08:40 AM', '09:00 AM', 1, '1', 1, 99, 1);
INSERT INTO cita(id_cita, fecha, hora_inicio, hora_final, estado, tipo, id_consultorio, id_medico, id_turno) VALUES (4, '2022-01-01', '09:00 AM', '09:20 AM', 1, '1', 1, 99, 1);
INSERT INTO cita(id_cita, fecha, hora_inicio, hora_final, estado, tipo, id_consultorio, id_medico, id_turno) VALUES (5, '2022-01-01', '09:20 AM', '09:40 AM', 1, '1', 1, 99, 1);
INSERT INTO cita(id_cita, fecha, hora_inicio, hora_final, estado, tipo, id_consultorio, id_medico, id_turno) VALUES (6, '2022-01-01', '09:40 AM', '10:00 AM', 1, '1', 1, 99, 1);
INSERT INTO cita(id_cita, fecha, hora_inicio, hora_final, estado, tipo, id_consultorio, id_medico, id_turno) VALUES (7, '2022-01-01', '10:00 AM', '10:20 AM', 1, '1', 1, 99, 1);
INSERT INTO cita(id_cita, fecha, hora_inicio, hora_final, estado, tipo, id_consultorio, id_medico, id_turno) VALUES (8, '2022-01-01', '10:20 AM', '10:40 AM', 1, '1', 1, 99, 1);
INSERT INTO cita(id_cita, fecha, hora_inicio, hora_final, estado, tipo, id_consultorio, id_medico, id_turno) VALUES (9, '2022-01-01', '10:40 AM', '11:00 AM', 1, '1', 1, 99, 1);
INSERT INTO cita(id_cita, fecha, hora_inicio, hora_final, estado, tipo, id_consultorio, id_medico, id_turno) VALUES (10, '2022-01-01', '11:00 AM', '11:20 AM', 1, '1', 1, 99, 1);
INSERT INTO cita(id_cita, fecha, hora_inicio, hora_final, estado, tipo, id_consultorio, id_medico, id_turno) VALUES (12, '2022-01-01', '11:20 AM', '11:40 AM', 1, '1', 1, 99, 1);
INSERT INTO cita(id_cita, fecha, hora_inicio, hora_final, estado, tipo, id_consultorio, id_medico, id_turno) VALUES (13, '2022-01-01', '11:40 AM', '12:00 AM', 1, '1', 1, 99, 1);
INSERT INTO cita(id_cita, fecha, hora_inicio, hora_final, estado, tipo, id_consultorio, id_medico, id_turno) VALUES (14, '2022-01-01', '12:00 PM', '12:20 PM', 1, '1', 1, 99, 1);
INSERT INTO cita(id_cita, fecha, hora_inicio, hora_final, estado, tipo, id_consultorio, id_medico, id_turno) VALUES (15, '2022-01-01', '12:20 PM', '12:40 PM', 1, '1', 1, 99, 1);
INSERT INTO cita(id_cita, fecha, hora_inicio, hora_final, estado, tipo, id_consultorio, id_medico, id_turno) VALUES (16, '2022-01-01', '12:40 PM', '01:00 PM', 1, '1', 1, 99, 1);



```


