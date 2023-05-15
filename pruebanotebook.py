from __future__ import annotations
from tkinter import *
from tkinter import ttk


root = Tk()
root.geometry("500x300")

tab1 = Frame(root)
tab2 = Frame(root)

# Mostrar la primera pestaña al inicio
tab1.pack()

# Contenido de la pestaña 1
label1 = Label(tab1, text='Bienvenido a mi programa.')
label1.pack(padx=10, pady=10)

# Botón para cambiar a la pestaña 2
button1 = Button(tab1, text='Menú', command=lambda: cambiar_pestaña(tab1, tab2))
button1.pack(padx=10, pady=10)

# Contenido de la pestaña 2
label2 = Label(tab2, text='Menú')
label2.pack(padx=10, pady=10)

# Botón para cambiar a la pestaña 1
button2 = Button(tab2, text='Regresar', command=lambda: cambiar_pestaña(tab2, tab1))
button2.pack(padx=10, pady=10)

# Función para cambiar de pestaña
def cambiar_pestaña(pestaña_actual, nueva_pestaña):
    pestaña_actual.pack_forget()
    nueva_pestaña.pack()

root.mainloop()