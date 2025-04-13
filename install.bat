@echo off
@echo ---------------------------------------------------
@echo              Instalador Di Gue 📦
@echo                    0t4v14n0
@echo ---------------------------------------------------
@echo.

:: Instala OCR
@echo ---------------------------------------------------
@echo  Instalando o OCR TESSERACT...
@echo  Garanta que a instalacao fique em:
@echo  "C:\\Program Files (x86)\\Tesseract-OCR"
@echo ---------------------------------------------------
pause
start /wait "" "resources\tesseract-ocr-setup-3.02.02.exe"

:: Verifica se Python está instalado
@echo.
@echo ---------------------------------------------------
@echo  Verificando instalacao do Python...
@echo ---------------------------------------------------
where python >nul 2>nul
if errorlevel 1 (
    echo Python nao encontrado. Instalando...
    start /wait "" "resources\python-3.13.0-amd64.exe" /quiet InstallAllUsers=1 PrependPath=1 Include_pip=1
) else (
    echo Python ja esta instalado.
)

:: Verifica se pip esta disponivel
@echo.
@echo ---------------------------------------------------
@echo  Instalando as bibliotecas necessarias...
@echo ---------------------------------------------------
pause
where pip >nul 2>nul
if errorlevel 1 (
    echo pip nao encontrado. Tentando com python -m pip...
    python -m pip install -r resources\bibliotecas.txt
) else (
    pip install -r resources\bibliotecas.txt
)

@echo ---------------------------------------------------
@echo Instalação finalizada!
pause
