#from Core import VentanasLogin

from configparser import ConfigParser
archivo='config.ini'

config = ConfigParser()
config.read(archivo)

print(config.sections())

