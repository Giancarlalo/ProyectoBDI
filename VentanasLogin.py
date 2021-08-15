# Imports ---------------

#from os import name
from tkinter.constants import BOTTOM, RIGHT
from guizero import App, Text, Waffle, Window , PushButton, TextBox, Box
from random import randint
import random
from datetime import datetime
import configparser
from tabulate import tabulate

# ------------------------------
# Conexión con la base de datos
# ------------------------------
from Core.ConfigConnection import ConfigConnection
from Core.MySQLEngine import MySQLEngine

configDB = configparser.ConfigParser()
configDB.read('Config/config.ini')

db=configDB['database']
config=ConfigConnection(db['host'],db['port'],db['user'],db['password'],db['database'])


engine = MySQLEngine(config)

# ------------------------------
# Funciones del Engine
# ------------------------------
def insertUser():
    t = engine.searchUser(nombreUsuario.value)
    # Condición de la inserción:
    if t == 0:
        #No existe el usuario en la base de datos:
        engine.insert_user(nombreUsuario.value,contraseña1.value)
        app.info("Advertencia","EL usuario ha sido agregado")
    else:
        app.info("Advertencia","El usuario con nombre "+ nombreUsuario.value +" ya existe")

# Por medio de este id guardaremos al usuario que se ingresó en las tablas score y bitacora

def userLogin():
    t = engine.searchUser(nombre.value)
    # Condición del login:
    if t == 0:
        #No existe el usuario en la base de datos:
        app.info("Advertencia","El usuario "+ nombre.value +" no está registrado")
        
    else:
        # El usuario existe, comprobamos la contraseña:
        t = engine.comparePassword(nombre.value,contrasena.value)
        if t == 0:
            app.info("Advertencia","Contraseña incorrecta, intente de nuevo")
        else:
        # Obtenemos el nombre del usuario para mostrar:
    
            mostrar_choice()

def isAdmin(name):
    if engine.isAdmin(name) == 1:
        print("Es administrador")
    else:
        print("No es admin")

# Muestra la tabla de puntajes:
def showScores():
    score = engine.showScore()

    for y in score:
        score_box = Box(window_puntaje,align="top",width="fill")
        for z in range(4):
            Text(score_box,text=y[z],align="left",width="fill",grid=[0,0])

def showBitacora():
    data = engine.showBitacora()
    for y in data:
        score_box = Box(window_bitacora,align="top",width="fill")
        for z in range(3):
            Text(score_box,text=y[z],align="left",width="fill",grid=[0,0])



# ------------------------------
# Variables Flood IT
# ------------------------------

colours = ["red", "blue", "green", "yellow", "magenta", "purple"]
board_size = 14
moves_limit = 25
moves_taken = 0

# ------------------------------
# Functions Flood IT
# ------------------------------

# Recursively floods adjacent squares
def flood(x, y, target, replacement):
    # Algorithm from https://en.wikipedia.org/wiki/Flood_fill
    if target == replacement:
        return False
    if board.get_pixel(x, y) != target:
        return False
    board.set_pixel(x, y, replacement)
    if y+1 <= board_size-1:   # South
        flood(x, y+1, target, replacement)
    if y-1 >= 0:            # North
        flood(x, y-1, target, replacement)
    if x+1 <= board_size-1:    # East
        flood(x+1, y, target, replacement)
    if x-1 >= 0:            # West
        flood(x-1, y, target, replacement)

# Check whether all squares are the same
def all_squares_are_the_same():
    squares = board.get_all()
    if all(colour == squares[0] for colour in squares):
        return True
    else:
        return False

def win_check():
    global moves_taken
    moves_taken += 1
    # Usuario jugando
    idUser = engine.getId(nombre.value)
    if moves_taken <= moves_limit:
        if all_squares_are_the_same():
            #Registramos en la base de datos
            date = datetime.now()
            print(date)
            print("Perdimos: " + str(idUser))
            engine.insertScore(score,date,2,idUser)
            win_text.value = "You win!"
    else:
            #Registramos en la base de datos
            date = datetime.now()
            print(date)
            print("Perdimos: " + str(idUser))
            engine.insertScore(score,date,2,idUser)
            win_text.value = "You lost :("


def fill_board():
    for x in range(board_size):
        for y in range(board_size):
            board.set_pixel(x, y, random.choice(colours))

def init_palette():
    for colour in colours:
        palette.set_pixel(colours.index(colour), 0, colour)

def start_flood(x, y):
    flood_colour = palette.get_pixel(x,y)
    target = board.get_pixel(0,0)
    flood(0, 0, target, flood_colour)
    win_check()

# Variables Destroy The Dots-------------

GRID_SIZE = 5
score = 0
Guadado=0
contador=0
nameUser = ""

# Functions Destroy The Dots------------- 

def add_dot():
    # Usuario jugando
    idUser = engine.getId(nombre.value)
    x, y = randint(0,GRID_SIZE-1), randint(0,GRID_SIZE-1)
    while board1[x, y].dotty == True:
        x, y = randint(0,GRID_SIZE-1), randint(0,GRID_SIZE-1)
    board1[x, y].dotty = True
    board1.set_pixel(x, y, "red")
    
    speed = 1000
    if score > 30:
        speed = 200
    elif score > 20:
        speed = 400
    elif score > 10:
        speed = 500
    elif score == -1:
        speed=0
    
    all_red = True
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            if board1[x,y].color != "red":
                all_red = False
    if all_red:
        score_display.value = "You lost! Score: " + str(score)
        #Registramos en la base de datos
        date = datetime.now()
        print(date)
        print("Perdimos: " + str(idUser))
        engine.insertScore(score,date,1,idUser)

    else:
        board1.after(speed, add_dot)

def destroy_dot(x,y):
    global score
    if board1[x,y].dotty == True:
        board1[x,y].dotty = False
        board1.set_pixel(x, y, "white")
        score += 1
        score_display.value = "Your score is " + str(score)

def stop_dot():
    board1.set_all("red")
    board1.dotty=False

def Continuar_Juego1():
    board1.set_all("white")
    board1.dotty=False
    add_dot()
    score_display.value = "Your score is " + str(score)
    window_comprobar.hide()
    window_game1.show()
    

def GuardarPartida1():

    Guardado=score
    board1.set_all("white")
    board1.dotty=False

    boxdoble.visible=True
    Reanudar=PushButton(boxdoble,text="Reanudar última partida",grid=[0,0],command=Continuar_Juego1)
    Icono=Text(boxdoble,text="▶",size=40,color="green",grid=[1,0])
    window_game1.hide()
    window_comprobar.hide()
    window_choice.show()




#Funcion de Botones
def mostrar_bitacora():
    showBitacora()
    window_bitacora.show()

def mostrar_puntaje():
    showScores()
    window_puntaje.show()

def comprobacion():
    stop_dot()
    window_comprobar.show()

def comprobacion2():
    window_comprobar2.show()

def mostrar_login():
    window_login.show() 

def mostrar_choice():
    window_login.hide()
    window_choice.show()
    
def mostrar_registro():
    window_login.hide()
    window_registro.show()

def iniciar_juego1():
    board1.after(100,add_dot)
    Iniciar.hide()

def mostrar_juego1():
    #
    print("Mostrar Juego1 " + nombre.value)
    name_display = Text(window_game1,text= "Id: " + str(engine.getId(nombre.value)) +" - usuario: " + nombre.value,grid=[0,0])
    window_game1.show()    

def mostrar_juego2():
    window_game2.show() 
    
def cerrar_Splash():
    app.hide()


# App -------------------
app = App(bg="Purple",height="700",width="800")
box2=Box(app,width="fill",height="300")
box=Box(app,width="fill",height="fill")
Bienvenida_label=Text(box,text="¡BIENVENIDO!",size=80,color="white",font="Comic Sans MS")
cargando_label=Text(box,text="Loading.....",size=30)
App.after(app,1500,mostrar_login)

#Windows------------------------------------------

window_bitacora = Window(app,bg="medium violet red", title="Bitacora")
window_bitacora.hide()

window_puntaje = Window(app, bg="medium violet red", title="Puntajes")
window_puntaje.hide()

window_game1 = Window(app, bg="#788199", title="Destroy The dots")
window_game1.hide()

window_game2 = Window(app, bg="#788199", title="Flood It")
window_game2.hide()

window_login = Window(app,bg="medium violet red",title="Pantalla de Login")
window_login.hide()

window_choice = Window(app, bg="bisque", title="Seleccione un Juego")
window_choice.hide()

window_registro= Window(app,bg="bisque", title="Registro")
window_registro.hide()

window_comprobar= Window(app,bg="#666666",title="Dialogbox",height=200,width=350)
window_comprobar.hide()

window_comprobar2= Window(app,bg="#666666",title="Dialogbox",height=200,width=350)
window_comprobar2.hide()

window_administrador=Window(app,bg="#788199",title="Modo Administrador")
window_administrador.hide()


#Destroy The Dots
titulo=Text(window_game1,text="DESTROY THE DOTS",size=30)
instructions = Text(window_game1, text="Click the dots to destroy them")
board1 = Waffle(window_game1, width=GRID_SIZE, height=GRID_SIZE, command=destroy_dot)
score_display = Text(window_game1, text="Your score is " + str(score))
box=Box(window_game1,width="fill",height="20")
Iniciar=PushButton(window_game1,text="Iniciar Juego",command=iniciar_juego1)
box=Box(window_game1,width="fill",height="20")
Detener=PushButton(window_game1,text="Finalizar Juego",command=comprobacion)

#Flood IT
titulo=Text(window_game2,text="FLOOD IT",size=30)
board = Waffle(window_game2, width=board_size, height=board_size, pad=0)
palette = Waffle(window_game2, width=6, height=1, dotty=True, command=start_flood)
win_text = Text(window_game2)
box=Box(window_game2,width="fill",height="20")
Detener=PushButton(window_game2,text="Finalizar Juego",command=comprobacion2)
fill_board()
init_palette()


#Window_login
box=Box(window_login,width="fill",height=200)
text_nombre=Text(window_login,text="Ingrese su nombre de usuario",color="White",size=10)
# Caja de texto del nombre de usuario
nombre=TextBox(window_login,text="Nombre usuario",width=30)
box=Box(window_login,width="fill",height=30)
text_nombre=Text(window_login,text="Ingrese su contraseña",color="White",size=10)
# Caja de texto de la contraseña
contrasena=TextBox(window_login,text="Ingrese su Contraseña",width=30,hide_text=True)
box=Box(window_login,width="fill",height=30)
#Botón de ingresar
ingresar_button =  PushButton(window_login, text="Ingresar", command=userLogin)
box=Box(window_login,width="fill",height=30)
registrar_button = PushButton(window_login, text="Registrar",command=mostrar_registro)


#Window_choice
box=Box(window_choice,width="fill",height=120)


#Llamar a la base de datos y pasarle el dato de score
if(score==0):
 boxdoble=Box(window_choice,width=190,height=60 ,layout="grid",grid=[0,0],visible=False)
 Reanudar=PushButton(boxdoble,text="Reanudar última partida",grid=[0,0])
 Icono=Text(boxdoble,text="▶",size=40,color="green",grid=[1,0])
else: 
    boxdoble=Box(window_choice,width=190,height=60 ,layout="grid",grid=[0,0],visible=True)
    Reanudar=PushButton(boxdoble,text="Reanudar última partida",grid=[0,0],command=Continuar_Juego1)
    Icono=Text(boxdoble,text="▶",size=40,color="green",grid=[1,0])
    window_game1.hide()
    window_comprobar.hide()
    window_choice.show()

box=Box(window_choice,width="fill",height=30)
boxdoble2=Box(window_choice,width=220,height=60 ,layout="grid",grid=[0,0])
Destroy_button =  PushButton(boxdoble2, text="DESTROY THE DOTS",grid=[1,0], command=mostrar_juego1)
Icono=Text(boxdoble2,text="0",size=30,color="red",grid=[0,0])
Icono=Text(boxdoble2,text="0",size=30,color="red",grid=[3,0])

box=Box(window_choice,width="fill",height=30)
boxdoble3=Box(window_choice,width=180,height=60 ,layout="grid",grid=[0,0])
Icono=Text(boxdoble3,text="¿",size=30,color="blue",grid=[0,0])
Flood_button = PushButton(boxdoble3, text="FLOOD IT", command=mostrar_juego2,grid=[1,0])
Icono=Text(boxdoble3,text="¿",size=30,color="blue",grid=[3,0])

box=Box(window_choice,width="fill",height=30)
boxdoble2=Box(window_choice,width=180,height=60 ,layout="grid",grid=[0,0])
# Botón para mostrar puntajes:
Destroy_button =  PushButton(boxdoble2, text="Puntajes",grid=[1,0], command=mostrar_puntaje)
Icono=Text(boxdoble2,text="?",size=30,color="black",grid=[0,0])
Icono=Text(boxdoble2,text="?",size=30,color="black",grid=[3,0])

#Window_Registro
box1=Box(window_registro,width="fill")
back=PushButton(box1,text="<-",align="left",command=mostrar_login and window_registro.hide)
titulo=Text(window_registro,text="'Ingrese los datos solicitados'",color="Black",size=15)
box1=Box(window_registro,width="fill",height=60)
# Caja de texto nombre del registro
nombreUsuario=TextBox(window_registro,text="Nombre de Usuario",width=50)
box1=Box(window_registro,width="fill",height=20)
# Caja de texto contraseña del registro
contraseña1=TextBox(window_registro,text="Ingrese Contraseña",width=50)
box1=Box(window_registro,width="fill",height=40)

#Aquí guardar los datos del registro en la base de datos--------------------------------------------------------------
Registrarse=PushButton(window_registro,text="Registrarse",command=insertUser)

#Window_comprobacion
box=Box(window_comprobar,width="fill",height=20)
back=PushButton(box,text="X",align="right")
texto=Text(window_comprobar,text="¿Seguro quiere finalizar el juego?",size=12,color="white")
box=Box(window_comprobar,width="fill",height=40)
box2=Box(window_comprobar,width="fill",height=120,layout="grid",grid=[1,0])
Espacio=Text(box2,text="                  ",grid=[0,0],enabled="false")
Cancelar=PushButton(box2,text="Cancelar",grid=[1,0],command=Continuar_Juego1)
Espacio=Text(box2,text="       ",grid=[2,0],enabled="false")
Aceptar=PushButton(box2,text="Aceptar",grid=[3,0], command=GuardarPartida1)

#Window_comprobacion2
box=Box(window_comprobar2,width="fill",height=20)
back=PushButton(box,text="X",align="right")
texto=Text(window_comprobar2,text="¿Seguro quiere finalizar el juego?",size=12,color="white")
box=Box(window_comprobar2,width="fill",height=40)
box2=Box(window_comprobar2,width="fill",height=120,layout="grid",grid=[1,0])
Espacio=Text(box2,text="                  ",grid=[0,0],enabled="false")
#Cancelar=PushButton(box2,text="𝘾𝙖𝙣𝙘𝙚𝙡𝙖𝙧",grid=[1,0],command=Continuar_Juego2)
Espacio=Text(box2,text="       ",grid=[2,0],enabled="false")
#Aceptar=PushButton(box2,text="𝘼𝙘𝙚𝙥𝙩𝙖𝙧",grid=[3,0], command=GuardarPartida2)

botonPrueba = PushButton(window_login,text="Bitacora",command=mostrar_bitacora)

def inicio():
    app.display()