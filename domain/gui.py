import tkinter as tk
from domain.screencap2 import *
from domain.deepseek2 import OpenRouter

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

        # Variável para armazenar o texto capturado original
        self.texto_capturado = ""

        # Campo de texto editável
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

        self.clear_btn = tk.Button(
            btn_frame,
            text="🗑️",
            command=self.limpar_tudo,
            bg="#555",
            fg="white",
            borderwidth=0,
            font=("Arial", 9),
            width=2
        )
        self.clear_btn.pack(side=tk.LEFT, padx=2)

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

    def restaurar_botoes(self):
        """Restaura todos os botões para o estado padrão"""
        self.capture_btn.config(text="🔍 Capturar", state=tk.NORMAL)
        self.send_btn.config(state=tk.NORMAL)
        self.update_idletasks()

    def iniciar_captura(self):
        try:
            # Configuração inicial
            self.capture_btn.config(text="...", state=tk.DISABLED)
            self.send_btn.config(state=tk.DISABLED)
            self.texto_resposta.delete("1.0", tk.END)
            self.texto_resposta.insert(tk.END, "Processando captura...")
            self.update_idletasks()
            
            # Executa a captura
            ScreenCapture(gui_reference=self)
            
        except Exception as e:
            self.mostrar_erro(f"Erro na captura: {str(e)}")
        finally:
            self.restaurar_botoes()

    def mostrar_resposta(self, texto):
        """Mostra o texto capturado pelo OCR"""
        self.texto_capturado = texto.strip()
        self.texto_resposta.delete("1.0", tk.END)
        self.texto_resposta.insert(tk.END, f"Texto capturado:\n{self.texto_capturado}")
        self.ajustar_tamanho()
        self.restaurar_botoes()

    def mostrar_resposta_api(self, resposta):
        """Adiciona a resposta da API ao texto existente"""
        resposta_formatada = f"\n\n--- Resposta ---\n{resposta.strip()}"
        self.texto_resposta.insert(tk.END, resposta_formatada)
        self.ajustar_tamanho()
        self.restaurar_botoes()

    def mostrar_erro(self, mensagem):
        """Mostra mensagens de erro"""
        self.texto_resposta.delete("1.0", tk.END)
        self.texto_resposta.insert(tk.END, f"ERRO: {mensagem}")
        self.ajustar_tamanho()
        self.restaurar_botoes()

    def ajustar_tamanho(self):
        """Ajusta o tamanho da janela conforme o conteúdo"""
        self.geometry("")
        
    def limpar_tudo(self):
        """Limpa todo o conteúdo"""
        self.texto_resposta.delete("1.0", tk.END)
        self.texto_capturado = ""
        self.ajustar_tamanho()

    def enviar_para_api(self):
        if not self.texto_capturado:
            self.mostrar_erro("Nenhum texto capturado para enviar")
            return

        try:
            self.send_btn.config(text="...", state=tk.DISABLED)
            self.capture_btn.config(state=tk.DISABLED)
            self.texto_resposta.insert(tk.END, "\n\nEnviando para API...")
            self.update_idletasks()
            
            OpenRouter.inicio(self.texto_capturado, gui_reference=self)
            
        except Exception as e:
            self.mostrar_erro(f"Erro na API: {str(e)}")
        finally:
            self.restaurar_botoes()