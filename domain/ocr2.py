import pytesseract as pt
import cv2
from pathlib import Path
from PIL import Image
from domain.deepseek import OpenRouter

class OCR:
    @staticmethod
    def inicio(gui_reference=None):
            
        pt.pytesseract.tesseract_cmd = "C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"

        img = cv2.imread('captura.png')
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

        cv2.imwrite("temp.png", thresh)
        text = pt.pytesseract.image_to_string(Image.open("temp.png"))
            
        if gui_reference:
            gui_reference.mostrar_resposta(text)
