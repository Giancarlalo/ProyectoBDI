import configparser

from Core.ConfigConnection import ConfigConnection
from Core.MySQLEngine import MySQLEngine
from Core import VentanasLogin

configDB = configparser.ConfigParser()
configDB.read('Config/config.ini')

db=configDB['database']
config=ConfigConnection(db['host'],db['port'],db['user'],db['password'],db['database'])


engine = MySQLEngine(config)


engine.insertar_usuario(VentanasLogin.varName,VentanasLogin.varPass)


#engine.verificar_usuario(VentanasLogin.varName,VentanasLogin.varPass)


VentanasLogin.app.display()