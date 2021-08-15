DROP DATABASE IF EXISTS Proyecto;
CREATE DATABASE Proyecto CHARACTER SET utf8;
USE Proyecto;

CREATE TABLE Roles(
    id INT AUTO_INCREMENT PRIMARY KEY,
    tex_nameRole VARCHAR(50) NOT NULL
);

CREATE TABLE Game(
    id INT AUTO_INCREMENT PRIMARY KEY,
    tex_nameGame VARCHAR(50) NOT NULL
);

CREATE TABLE User(
    id INT AUTO_INCREMENT PRIMARY KEY,
    tex_name VARCHAR(100) NOT NULL,
    tex_password VARCHAR(100) NOT NULL,
    int_idRole_fk INT,
    FOREIGN KEY (int_idRole_fk) REFERENCES Roles(id)
);

CREATE TABLE Score(
    id INT AUTO_INCREMENT PRIMARY KEY,
    int_points INT NOT NULL,
    dat_time DATETIME(2),
    int_idGame_fk INT,
    int_idUser_fk INT,
    FOREIGN KEY (int_idGame_fk) REFERENCES Game(id),
    FOREIGN KEY (int_idUser_fk) REFERENCES User(id)
);

CREATE TABLE Bitacora(
    id SERIAL PRIMARY KEY,
    tex_accion TEXT,
    int_idUser_fk INT,
    dat_time DATETIME(2),
    FOREIGN KEY (int_idUser_fk) REFERENCES User(id)
);

-- Insertamos los roles (Hay que hacer la funcio que lo ejecute todo al iniciar por primera vez el programa)
INSERT INTO Roles(tex_nameRole) VALUES('Admin');
INSERT INTO Roles(tex_nameRole) VALUES ('Jugador');

-- Insertamos los juegos (Igualmente hay que hacer una función)
INSERT INTO Game(tex_nameGame) VALUES('Destroy The Dots');
INSERT INTO Game(tex_nameGame) VALUES ('Flood It');

-- Insertamos el primer usuario como admin:
INSERT INTO User(tex_name, tex_password, int_idRole_fk) VALUES ('Alonso','eduka',1);

-- Tabla Bitacora:
INSERT INTO Bitacora(tex_accion,int_idUser_fk,dat_time) VALUES ("Aqui comienza la bitacora",1,NOW());

-- Triggers para el ingreso de datos en la tabla de bitacora:

-- El admin al ingresar un nuevo usuario:
CREATE TRIGGER insert_user AFTER INSERT ON User FOR EACH ROW 
INSERT INTO Bitacora(tex_accion,int_idUser_fk,dat_time) VALUES (" usuario ha iniciado sesion",1,NOW());

-- Al ingresar un score:
CREATE TRIGGER insert_score AFTER INSERT ON Score FOR EACH ROW 
INSERT INTO Bitacora(tex_accion,int_idUser_fk,dat_time) VALUES ("El usuario ha jugado",1,NOW());

SELECT t2.tex_name AS "Nombre del usuario", t1.tex_accion AS "Acción", t1.dat_time AS "Fecha" FROM Bitacora AS t1
JOIN User AS t2 ON t1.int_idUser_fk = t2.id;

SELECT * FROM Roles;
SELECT * FROM Game;
SELECT * FROM Score;
SELECT * FROM User;
SELECT * FROM Bitacora;

SELECT t1.tex_name AS "Nombre de usuario", t2.tex_nameGame AS "Juego", t3.int_points AS "Puntaje", t3.dat_time AS"Fecha de juego" FROM Score AS t3
JOIN User AS t1 ON t3.int_idUser_fk = t1.id
JOIN Game AS t2 ON t3.int_idGame_fk = t2.id;