from __future__ import annotations
import tkinter as tk
from tkinter import ttk

class contenido1:
    def __init__(self, adm: admVentanas, c2: contenido2):
        self.c2 = c2
        self.adm = adm
        self.frame = tk.Frame(adm.ventana)
        button1 = ttk.Button(self.frame, text='Menú', command=lambda: self.adm.cambiar_pestaña(self, self.c2))
        button1.pack(padx=10, pady=10)
        
    def pack(self):
        self.frame.pack()

class contenido2:
    def __init__(self, adm: admVentanas, c1: contenido1):
        self.adm = adm
        self.frame = tk.Frame(adm.ventana)
        self.c1 = c1
        button2 = ttk.Button(self.frame, text='Men', command=lambda: self.adm.cambiar_pestaña(self, self.c1))
        button2.pack(padx=10, pady=10)
    def pack(self):
        self.frame.pack()

class admVentanas:
    def __init__(self):
        self.ventana = tk.Tk()
        self.contenido1 = contenido1(self, contenido2(self, None))
        self.contenido2 = contenido2(self, self.contenido1)

    def cambiar_pestaña(self, pestaña_actual, nueva_pestaña):
        pestaña_actual.frame.pack_forget()
        nueva_pestaña.pack()

    def start(self):
        self.contenido1.pack()

adm = admVentanas()
adm.start()
adm.ventana.mainloop()