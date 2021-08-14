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

CREATE TABLE Score(
    id INT AUTO_INCREMENT PRIMARY KEY,
    int_points INT NOT NULL,
    dat_time DATETIME(2),
    int_idGame_fk INT,
    FOREIGN KEY (int_idGame_fk) REFERENCES Game(id)
);

CREATE TABLE User(
    id INT AUTO_INCREMENT PRIMARY KEY,
    tex_name VARCHAR(100) NOT NULL,
    tex_password VARCHAR(100) NOT NULL,
    int_idRole_fk INT,
    FOREIGN KEY (int_idRole_fk) REFERENCES Score(id)
);

CREATE TABLE Bitacora(
    id SERIAL PRIMARY KEY,
    tex_accion TEXT,
    int_idUser_fk INT,
    FOREIGN KEY (int_idUser_fk) REFERENCES User(id)
);


INSERT INTO Roles(tex_nameRole) VALUES('Admin');
INSERT INTO Game(tex_nameGame) VALUES('Dots');
INSERT INTO Score(int_points,int_idGame_fk) VALUES(0,1);

INSERT INTO User(tex_name, tex_password , int_idRole_fk) VALUES ('Alonso','eduka',1);

INSERT INTO Bitacora(tex_accion,int_idUser_fk) VALUES ("Aqui comienza la bitacora",1);



SELECT * FROM Roles;
SELECT *FROM Game;
SELECT * FROM Score;
SELECT * FROM User;

SELECT * FROM Bitacora;

