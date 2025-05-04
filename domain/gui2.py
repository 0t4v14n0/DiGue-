import tkinter as tk
from tkinter import font
from domain.screencap import *

class MinhaApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Pergunta DI GUE ?")
        self.geometry("200x50")  # Bem pequeno
        self.attributes('-alpha', 0.9)  # Levemente transparente
        self.attributes('-topmost', True)  # Fica sobre outras janelas
        
        # Remove decorações da janela
        self.overrideredirect(True)
        
        # Posiciona no canto superior direito
        screen_width = self.winfo_screenwidth()
        self.geometry(f"+{screen_width-210}+10")
        
        # Container principal
        self.frame = tk.Frame(self, bg='#333333')
        self.frame.pack(fill=tk.BOTH, expand=True)
        
        # Botão de captura (pequeno)
        self.capture_btn = tk.Button(
            self.frame,
            text="🔍",  # Ícone de lupa
            command=self.iniciar_captura,
            bg='#444444',
            fg='white',
            borderwidth=0,
            font=("Arial", 10),
            width=3
        )
        self.capture_btn.pack(side=tk.LEFT, padx=2, pady=2)
        
        # Label para a resposta (inicialmente vazio)
        self.resposta_label = tk.Label(
            self.frame,
            text="",
            bg='#333333',
            fg='white',
            font=("Arial", 10),
            wraplength=150
        )
        self.resposta_label.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        
        # Botão de fechar (mini)
        self.close_btn = tk.Button(
            self.frame,
            text="×",
            command=self.destroy,
            bg='#444444',
            fg='white',
            borderwidth=0,
            font=("Arial", 8),
            width=2
        )
        self.close_btn.pack(side=tk.RIGHT, padx=2, pady=2)
        
        # Permite mover a janela
        self.bind("<ButtonPress-1>", self.start_move)
        self.bind("<B1-Motion>", self.on_move)
    
    def start_move(self, event):
        self._x = event.x
        self._y = event.y
    
    def on_move(self, event):
        x = self.winfo_x() + (event.x - self._x)
        y = self.winfo_y() + (event.y - self._y)
        self.geometry(f"+{x}+{y}")
    
    def iniciar_captura(self):
        self.capture_btn.config(text="...")  # Feedback visual
        self.resposta_label.config(text="")
        self.update()
        ScreenCapture(gui_reference=self)
    
    def mostrar_resposta(self, texto):
        self.capture_btn.config(text="🔍")  # Restaura ícone
        self.resposta_label.config(text=texto)
        # Auto-ajusta o tamanho da janela conforme o texto
        self.update_idletasks()
        self.geometry("")  # Redimensiona automaticamente