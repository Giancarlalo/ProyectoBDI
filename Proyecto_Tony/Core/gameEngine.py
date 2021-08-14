# -- coding: utf-8 --

# Imports para la base de datos
from Core.MySQLEngine import MySQLEngine
from Core.ConfigConnection import ConfigConnection

config = ConfigConnection(
    "localhost",
    "3306",
    "admin",
    "admin",
    "Proyecto"
)

mEngine = MySQLEngine(config)

class gameEngine:

    def _init_(self):
        pass
    
    def insertUser(self,name,password):
        query = ("INSERT INTO User (tex_name,tex_password) VALUES ({},{})".format(name,password))
        mEngine.executeQueries(query)
        print("Se he insertado el usuario {} con pass {}".format(name,password))

    def executeQueries(self,query):
        result = self.link.execute(query)
        print("Se ha ejecutado la transaccion '{}', con resultado: {}".format(query,result))
        return result