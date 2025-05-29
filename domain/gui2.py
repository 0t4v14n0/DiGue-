import tkinter as tk
from domain.screencap import *
from domain.deepseek import OpenRouter

class MinhaApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Pergunta DI GUE ?")
        self.geometry("300x150")
        self.attributes('-alpha', 0.95)
        self.attributes('-topmost', True)
        self.overrideredirect(True)

        screen_width = self.winfo_screenwidth()
        self.geometry(f"+{screen_width - 310}+10")

        self.frame = tk.Frame(self, bg='#2e2e2e')
        self.frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Campo de texto editável para mostrar e alterar a resposta
        self.texto_resposta = tk.Text(
            self.frame,
            height=4,
            font=("Arial", 10),
            wrap=tk.WORD,
            bg="#1e1e1e",
            fg="white",
            insertbackground="white",
            borderwidth=0
        )
        self.texto_resposta.pack(fill=tk.BOTH, expand=True)

        # Botões
        btn_frame = tk.Frame(self.frame, bg="#2e2e2e")
        btn_frame.pack(fill=tk.X, pady=2)

        self.capture_btn = tk.Button(
            btn_frame,
            text="🔍 Capturar",
            command=self.iniciar_captura,
            bg="#444",
            fg="white",
            borderwidth=0,
            font=("Arial", 9)
        )
        self.capture_btn.pack(side=tk.LEFT, padx=2)

        self.send_btn = tk.Button(
            btn_frame,
            text="📤 Enviar",
            command=self.enviar_para_api,
            bg="#3c7",
            fg="white",
            borderwidth=0,
            font=("Arial", 9)
        )
        self.send_btn.pack(side=tk.LEFT, padx=2)

        self.close_btn = tk.Button(
            btn_frame,
            text="×",
            command=self.destroy,
            bg="#844",
            fg="white",
            borderwidth=0,
            font=("Arial", 9),
            width=2
        )
        self.close_btn.pack(side=tk.RIGHT, padx=2)

        # Movimento da janela
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
        self.capture_btn.config(text="...")
        self.texto_resposta.delete("1.0", tk.END)
        self.update()
        ScreenCapture(gui_reference=self)

    def mostrar_resposta(self, texto):
        self.capture_btn.config(text="🔍 Capturar")
        self.texto_resposta.delete("1.0", tk.END)
        self.texto_resposta.insert(tk.END, texto)
        self.geometry("")  # Auto-ajusta tamanho

    def enviar_para_api(self):
        texto = self.texto_resposta.get("1.0", tk.END).strip()
        if texto:
            print("[Enviando para API]:", texto)
            OpenRouter.inicio(texto, gui_reference=self)
