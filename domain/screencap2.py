from tkinter import *
from PIL import ImageGrab
from domain.ocr2 import *

class ScreenCapture:
    def __init__(self, gui_reference=None):
        self.gui = gui_reference
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
        OCR.inicio(gui_reference=self.gui)
    