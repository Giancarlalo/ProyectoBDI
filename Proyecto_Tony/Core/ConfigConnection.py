# -*- coding: utf-8 -*-

class ConfigConnection:
    #El metodo constructor "init" recibe el self por defecto que seria un this
    def __init__(self,host,port,user,password,database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database