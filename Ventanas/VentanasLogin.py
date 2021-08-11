# Imports ---------------

from guizero import App, Text, Waffle, Window , PushButton, TextBox, info, Picture, Box
from random import randint
import random

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
    if moves_taken <= moves_limit:
        if all_squares_are_the_same():
            win_text.value = "You win!"
    else:
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

# Functions Destroy The Dots-------------


def add_dot():
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
    else:
        board1.after(speed, add_dot)

def destroy_dot(x,y):
    global score
    if board1[x,y].dotty == True:
        board1[x,y].dotty = False
        board1.set_pixel(x, y, "white")
        score += 1
        score_display.value = "Your score is " + str(score)


#Funcion de Botones
def comprobacion():
    window_comprobar.show()

def mostrar_login():
    window_login.show() 

def mostrar_choice():
    window_choice.show()
    
def mostrar_registro():
    window_registro.show()

def mostrar_juego1():
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
App.after(app,2000,mostrar_login)

#Windows------------------------------------------
window_game1 = Window(app,bg="#788199", title="𝘿𝙚𝙨𝙩𝙧𝙤𝙮 𝙏𝙝𝙚 𝘿𝙤𝙩𝙨")
window_game1.hide()

window_game2 = Window(app, title="𝙁𝙡𝙤𝙤𝙙 𝙄𝙩")
window_game2.hide()

window_login = Window(app,bg="medium violet red",title="Pantalla de Login")
window_login.hide()

window_choice = Window(app, bg="bisque", title="Seleccione un Juego")
window_choice.hide()

window_registro= Window(app,bg="bisque", title="Registro")
window_registro.hide()

window_comprobar= Window(app,bg="#666666",title="Dialogbox",height=200,width=350)
window_comprobar.hide()


#Destroy The Dots
titulo=Text(window_game1,text="🅳🅴🆂🆃🆁🅾🆈 🆃🅷🅴 🅳🅾🆃🆂",size=30)
instructions = Text(window_game1, text="Click the dots to destroy them")
board1 = Waffle(window_game1, width=GRID_SIZE, height=GRID_SIZE, command=destroy_dot)
board1.after(1000, add_dot)
score_display = Text(window_game1, text="Your score is " + str(score))
box=Box(window_game1,width="fill",height="20")
Detener=PushButton(window_game1,text="Finalizar Juego",command=comprobacion)

#Flood IT
board = Waffle(window_game2, width=board_size, height=board_size, pad=0)
palette = Waffle(window_game2, width=6, height=1, dotty=True, command=start_flood)
win_text = Text(window_game2)
fill_board()
init_palette()


#Window_login

box=Box(window_login,width="fill",height=200)
text_nombre=Text(window_login,text="Ingrese su nombre de usuario",color="White",size=10)
nombre=TextBox(window_login,text="Nombre usuario",width=30)
box=Box(window_login,width="fill",height=30)
text_nombre=Text(window_login,text="Ingrese su contraseña",color="White",size=10)
contrasena=TextBox(window_login,text="Ingrese su Contraseña",width=30,hide_text=True)
box=Box(window_login,width="fill",height=30)
ingresar_button =  PushButton(window_login, text="Ingresar", command=mostrar_choice)
box=Box(window_login,width="fill",height=30)
registrar_button = PushButton(window_login, text="Registrar",command=mostrar_registro)



#Window_choice
box=Box(window_choice,width="fill",height=120)
boxdoble=Box(window_choice,width=190,height=60 ,layout="grid",grid=[0,0],visible=False)
Reanudar=PushButton(boxdoble,text="Reanudar última partida",grid=[0,0])
Icono=Text(boxdoble,text="▶",size=40,color="green",grid=[1,0])

box=Box(window_choice,width="fill",height=30)
boxdoble2=Box(window_choice,width=220,height=60 ,layout="grid",grid=[0,0])
Destroy_button =  PushButton(boxdoble2, text="𝘿𝙚𝙨𝙩𝙧𝙤𝙮 𝙏𝙝𝙚 𝘿𝙤𝙩𝙨",grid=[1,0], command=mostrar_juego1)
Icono=Text(boxdoble2,text="🔴",size=30,color="red",grid=[0,0])
Icono=Text(boxdoble2,text="🔴",size=30,color="red",grid=[3,0])

box=Box(window_choice,width="fill",height=30)
boxdoble3=Box(window_choice,width=180,height=60 ,layout="grid",grid=[0,0])
Icono=Text(boxdoble3,text="🌊",size=30,color="blue",grid=[0,0])
Flood_button = PushButton(boxdoble3, text="𝙁𝙡𝙤𝙤𝙙 𝙄𝙩", command=mostrar_juego2,grid=[1,0])
Icono=Text(boxdoble3,text="🌊",size=30,color="blue",grid=[3,0])

#Window_Registro
box1=Box(window_registro,width="fill")
back=PushButton(box1,text="🢀",align="left",command=mostrar_login and window_registro.hide)
titulo=Text(window_registro,text="'Ingrese los datos solicitados'",color="Black",size=15)
box1=Box(window_registro,width="fill",height=60)
nombreUsuario=TextBox(window_registro,text="Nombre de Usuario",width=50)
box1=Box(window_registro,width="fill",height=20)
contraseña1=TextBox(window_registro,text="Ingrese Contraseña",width=50)
box1=Box(window_registro,width="fill",height=40)

#Aquí guardar los datos del registro en la base de datos--------------------------------------------------------------
Registrarse=PushButton(window_registro,text="Registrarse",command=mostrar_login and window_registro.hide)

#Window_comprobacion
box=Box(window_comprobar,width="fill",height=20)
back=PushButton(box,text="❌",align="right")
texto=Text(window_comprobar,text="¿Seguro quiere finalizar el juego?",size=12,color="white")
box=Box(window_comprobar,width="fill",height=40)
box2=Box(window_comprobar,width="fill",height=120,layout="grid",grid=[1,0])
Espacio=Text(box2,text="                  ",grid=[0,0],enabled="false")
Cancelar=PushButton(box2,text="𝘾𝙖𝙣𝙘𝙚𝙡𝙖𝙧",grid=[1,0])
Espacio=Text(box2,text="       ",grid=[2,0],enabled="false")
Aceptar=PushButton(box2,text="𝘼𝙘𝙚𝙥𝙩𝙖𝙧",grid=[3,0])


app.display()


