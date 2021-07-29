from guizero import App , Text, Window, PushButton
from time import sleep, time

def open_window():
    Window.show()

def close_window():
    Window.hide(wait=True)

def open_window():
    window.show(wait=True)
app = App(title="Bienvenida",bg="light blue")

window = Window(app, title = "2nd Window", height=300, width=200)
window.hide()


App.after(app,2000,open_window)
App.after(window,2000,close_window)

Text = Text(app, text="¡BIENVENIDO!", font='Serif', size=45, width="fill", height="fill")


app.display()
