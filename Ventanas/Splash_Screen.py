
from tkinter.constants import LEFT
from guizero import App , Text
from guizero.TextBox import TextBox
app = App(title="Bienvenida",bg="light blue")


Text = Text(app, text="¡BIENVENIDO!", font='Serif', size=45, width="fill", align=LEFT)


app.display()


