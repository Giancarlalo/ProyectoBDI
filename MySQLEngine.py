from datetime import datetime
import mysql.connector
import re
from tabulate import tabulate


class MySQLEngine:

    #Constructor
    def __init__(self,config):
        self.connect(config)

    #Metodo connect
    def connect(self,config):
        #self.mydb para que quede guardada en mi objeto
        self.mydb = mysql.connector.connect(
            host=config.host,
            port=config.port,
            user=config.user,
            password=config.password,
            database=config.database
        )

        self.link = self.mydb.cursor()   

    def install(self):
        query = """CREATE DATABASE Proyecto CHARACTER SET utf8;
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
        
        """
    def insert_user(self,name,password,rol=2):
        query="INSERT INTO User(tex_name, tex_password ,int_idRole_fk) VALUES ('%s','%s','%s');" % (name,password,rol)
        cursor=self.link
        cursor.execute(query)
        self.mydb.commit()
        print("Usuario insertado")
        self.mydb.close()
    
    # Cantidad de registros a mostrar
    def selectPage(self,query,page=0,count=25):
        #limpiar el query removiendo el Limit existente (el cual es opcional).
        query = re.sub(r"\s+[Ll][Ii][Mm][Ii][Tt]\s+\d+\s*(,\s*\d+)?\s*;?\s*$","",query)

        #reconstruir el query adicionando la nueva informacion solicitada.
        query = "{} LIMIT {},{};".format(query,page,count)
        print(query)
        #Ejecutar la instruccion en SQL.
        self.link.execute(query)
        return self.link.fetchall()

     # Mostrar como tabla
    def printAsTable(self,result,headers=[]):
        if not headers:
            return tabulate(result)
        else:
            return tabulate(result,headers=headers)
 

    # Devuelve 1 si el usuario existe y 0 si no:
    def searchUser(self, nombre):
        print(nombre)
        query = "SELECT COUNT(1) FROM User WHERE tex_name = '%s';" % (nombre)
        self.link.execute(query)
        t = self.link.fetchone()
        return t[0]

    # Devuelve 1 si el pasword conincide existe y 0 si no:
    def comparePassword(self, name, password):
        query = "SELECT COUNT(1) FROM User WHERE tex_name = '%s' AND tex_password = '%s';" % (name,password)
        self.link.execute(query)
        t = self.link.fetchone()
        return t[0]

    # Devuleve el id del Usuario
    def getId(self,nombre):
        query = "SELECT id FROM User WHERE tex_name = '%s';" % (nombre)
        self.link.execute(query)
        t = self.link.fetchone()
        return t[0]

    # Retorna el nombre del usuario:
    def getName(self,id):
        print(id)
        query = "SELECT tex_name FROM User WHERE id = '%s';" % (id)
        self.link.execute(query)
        t = self.link.fetchone()
        return t[0]

    def isAdmin(self,name):
        print(id)
        query = "SELECT int_idRole_fk FROM User WHERE tex_name= '%s';" % (name)
        self.link.execute(query)
        t = self.link.fetchone()
        return t[0]

    # Inserta en la tabla score al finalizar una partida:
    def insertScore(self,score,date,idJuego,idUser):
        query =  "INSERT INTO Score (int_points,dat_time,int_idGame_fk,int_idUser_fk) VALUES (%s,'%s',%s,%s);" % (score,date,idJuego,idUser)
        cursor=self.link
        cursor.execute(query)
        self.mydb.commit()
        print("Puntaje insertado")
        self.mydb.close()
    
    def showScore(self):
        query = """SELECT t1.tex_name AS "Nombre de usuario", t2.tex_nameGame AS "Juego", t3.int_points AS "Puntaje", t3.dat_time AS"Fecha de juego" FROM Score AS t3
                    JOIN User AS t1 ON t3.int_idUser_fk = t1.id
                    JOIN Game AS t2 ON t3.int_idGame_fk = t2.id
                    ORDER BY t3.int_points DESC;"""
        self.link.execute(query)
        self.mydb.close()
        return self.link.fetchall()
    
    def showBitacora(self):
        query ="""SELECT t2.tex_name AS "Nombre del usuario", t1.tex_accion AS "Acción", t1.dat_time AS "Fecha" FROM Bitacora AS t1
                    JOIN User AS t2 ON t1.int_idUser_fk = t2.id;"""
        self.link.execute(query)
        self.mydb.close()
        return self.link.fetchall()