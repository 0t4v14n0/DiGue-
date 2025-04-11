from tkinter import *
import pyautogui
from PIL import ImageGrab
import tkinter as tk
from tkinter import PhotoImage


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

class ScreenCapture:
    def __init__(self):
        self.start_x = None
        self.start_y = None
        self.rect = None
        self.root = Tk()
        self.root.attributes('-fullscreen', True)
        self.root.attributes('-alpha', 0.3)
        self.canvas = Canvas(self.root, cursor="cross", bg='gray')
        self.canvas.pack(fill=BOTH, expand=True)
        self.canvas.bind("<ButtonPress-1>", self.on_press)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)
        self.root.mainloop()

    def on_press(self, event):
        self.start_x = self.canvas.canvasx(event.x)
        self.start_y = self.canvas.canvasy(event.y)
        self.rect = self.canvas.create_rectangle(self.start_x, self.start_y, self.start_x, self.start_y, outline='red', width=2)

    def on_drag(self, event):
        cur_x, cur_y = (self.canvas.canvasx(event.x), self.canvas.canvasy(event.y))
        self.canvas.coords(self.rect, self.start_x, self.start_y, cur_x, cur_y)

    def on_release(self, event):
        end_x, end_y = (self.canvas.canvasx(event.x), self.canvas.canvasy(event.y))
        self.root.destroy()
        x1, y1 = int(min(self.start_x, end_x)), int(min(self.start_y, end_y))
        x2, y2 = int(max(self.start_x, end_x)), int(max(self.start_y, end_y))
        image = ImageGrab.grab(bbox=(x1, y1, x2, y2))
        image.save("captura.png")
        print("Imagem capturada e salva como captura.png")

class OCR:
    print("")

class IAResposta:
    print("")

if __name__ == "__main__":

    app = MinhaApp()
    app.mainloop()

