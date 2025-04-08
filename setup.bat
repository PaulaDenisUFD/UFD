@echo off
echo Creando el entorno virtual...
python -m venv .venv

echo Activando el entorno virtual...
call .venv\Scripts\activate

echo Instalando las dependencias desde requirements.txt...
pip install -r requirements.txt

echo El entorno virtual ha sido creado y las dependencias se han instalado correctamente.
pause
