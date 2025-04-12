import tkinter as tk
from tkinter import PhotoImage
from domain.screencap import *

class MinhaApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Pergunta DI GUE ?")
        self.geometry("500x500")
        
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        
        self.pagina_atual = None
        self.mostrar_pagina(PaginaInicial)
    
    def mostrar_pagina(self, pagina):
        nova_pagina = pagina(self.container, self)
        if self.pagina_atual is not None:
            self.pagina_atual.destroy()
        self.pagina_atual = nova_pagina
        self.pagina_atual.grid(row=0, column=0, sticky="nsew")

class PaginaInicial(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        self.img_menup = PhotoImage(file="imagens/inicio.png")

        self.labelfundo = tk.Label(self, image=self.img_menup)
        self.labelfundo.pack()

        submit_button = tk.Button(self, text="Capturar Pergunta", command=ScreenCapture,font=("Arial", 30))
        submit_button.place(x=70, y=350)