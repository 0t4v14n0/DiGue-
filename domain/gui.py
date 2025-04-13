import tkinter as tk
from tkinter import PhotoImage
from domain.screencap import *

class MinhaApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Pergunta DI GUE ?")
        self.geometry("500x500")
        self.iconbitmap("imagens/ico.ico")
        
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

        self.texto_resposta = tk.Text(self, height=5, width=10, font=("Arial", 12))
        self.texto_resposta.place(x=200, y=300)

        submit_button = tk.Button(
            self,
            text="Capturar Pergunta",
            command=lambda: [
                self.texto_resposta.delete("1.0", tk.END),  # Limpa o texto
                self.controller.iconify(),  # Minimiza a janela principal
                self.iniciar_captura()     # Inicia o processo de captura
            ],
            font=("Arial", 30)
        )
        submit_button.place(x=70, y=400)
    
    def iniciar_captura(self):
        # Passa self (esta instncia) para ScreenCapture
        ScreenCapture(gui_reference=self)

    def mostrar_resposta(self, texto):
        self.texto_resposta.delete("1.0", tk.END)  # Limpa o conteudo da caixa de texto
        self.texto_resposta.insert(tk.END, texto)

        self.controller.deiconify()  # Remove o estado minimizado
        self.controller.lift()       # Traz para frente de outras janelas