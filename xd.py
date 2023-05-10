import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('300x200')

# Crear el notebook y las pestañas
notebook = ttk.Notebook(root)
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)

notebook.add(tab1, text='Pestaña 1')
notebook.add(tab2, text='Pestaña 2')
ttk.Notebook.hide(tab1)
notebook.pack(expand=1, fill='both')

# Contenido de la pestaña 1
label1 = tk.Label(tab1, text='Contenido de la pestaña 1')
label1.pack(padx=10, pady=10)

# Contenido de la pestaña 2
label2 = tk.Label(tab2, text='Contenido de la pestaña 2')
label2.pack(padx=10, pady=10)

# Funciones para mostrar y ocultar pestañas
def mostrar_tab1():
    tab1.pack(expand=1, fill='both')
    tab2.pack_forget()

def mostrar_tab2():
    tab2.pack(expand=1, fill='both')
    tab1.pack_forget()

# Crear los botones para mostrar/ocultar pestañas
button1 = tk.Button(root, text='Mostrar pestaña 1', command=mostrar_tab1)
button1.pack(pady=10)
button2 = tk.Button(root, text='Mostrar pestaña 2', command=mostrar_tab2)
button2.pack(pady=10)

root.mainloop()