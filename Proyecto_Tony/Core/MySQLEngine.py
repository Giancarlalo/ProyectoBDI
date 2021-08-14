import mysql.connector
import re
from tabulate import tabulate
from Core import VentanasLogin



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

    def insertar_usuario(self,name,password,rol=1):
        query="INSERT INTO User(tex_name, tex_password ,int_idRole_fk) VALUES ('%s','%s','%s');" % (name,password,rol)
        cursor=self.link
        cursor.execute(query)
        self.mydb.commit()
        self.mydb.close()    

    def hello():
        VentanasLogin.name.value="hello"


    def verificar_usuario(self,name):
        pass 

    def search(self, nombre):
        print(nombre)
        query = "SELECT COUNT(1) FROM User WHERE tex_name = '%s';" % (nombre)
        self.link.execute(query)
        t = self.link.fetchone()
        return t[0]


