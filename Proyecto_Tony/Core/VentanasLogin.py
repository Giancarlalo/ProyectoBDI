# Imports ---------------

from guizero import App, Text, Waffle, Window , PushButton, TextBox, info
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
def mostrar_login():
    window_login.show() 

def mostrar_choice():
    window_choice.show()
    window_login.hide()

def mostrar_juego1():
    window_game1.show()    

def mostrar_juego2():
    window_game2.show() 



varName=""
varPass=""

def registrar_usuario():
    global varName
    varName=name_label.value
    global varPass
    varPass=password_label.value


def limpiar_labels(): 
    name_label.value=""
    password_label.value=""

# App -------------------

app = App("Bienvenido")
jugar_button = PushButton(app, text="Jugar", command=mostrar_login)

#Windows------------------------------------------
window_game1 = Window(app, title="Destroy The Dots")
window_game1.hide()

window_game2 = Window(app, title="Flood IT")
window_game2.hide()

window_login = Window(app, title="Pantalla de Login" , layout="grid")
window_login.hide()

window_choice = Window(app, title="Seleccione un Juego", layout="grid")
window_choice.hide()


#Destroy The Dots
instructions = Text(window_game1, text="Click the dots to destroy them")
board1 = Waffle(window_game1, width=GRID_SIZE, height=GRID_SIZE, command=destroy_dot)
board1.after(1000, add_dot)
score_display = Text(window_game1, text="Your score is " + str(score))

#Flood IT
board = Waffle(window_game2, width=board_size, height=board_size, pad=0)
palette = Waffle(window_game2, width=6, height=1, dotty=True, command=start_flood)
win_text = Text(window_game2)
fill_board()
init_palette()


#Window_login
name = Text(window_login, text="Username", grid=[0,0])
name_label = TextBox(window_login, grid=[1,0])
password = Text(window_login, text="Password", grid=[0,2])
password_label = TextBox(window_login, grid=[1,2])

ingresar_button =  PushButton(window_login, text="Ingresar",  command=mostrar_choice, grid=[0,3])
registrar_button = PushButton(window_login, text="Registrar", command=registrar_usuario, grid=[1,3])
limpiar_button = PushButton(window_login, text="Limpiar",command=limpiar_labels ,grid=[2,3])




#Window_choice

Destroy_button =  PushButton(window_choice, text="Destroy The Dots",  command=mostrar_juego1, grid=[0,1])
Flood_button = PushButton(window_choice, text="Flood IT", command=mostrar_juego2, grid=[1,1])





app.display()



