from pathlib import Path

# Definir rutas usando pathlib
RUTA_HOME = Path.home()  # Usamos el directorio home del usuario, puedes ajustarlo según sea necesario
RUTA_PROGRAMA = Path(__file__).resolve().parent

RUTA_DESCARGAS = RUTA_HOME / "Downloads"  # Ruta de la carpeta de descargas
RUTA_ENTRADA = RUTA_PROGRAMA / "input"  # Ruta de entrada
RUTA_SALIDA = RUTA_PROGRAMA / "output"  # Ruta de salida

# Definir archivos de entrada y salida
ARCHIVO_ENTRADA_1 = RUTA_ENTRADA / "archivo1.csv"
ARCHIVO_ENTRADA_2 = RUTA_ENTRADA / "archivo2.csv"
ARCHIVO_SALIDA = RUTA_SALIDA / "archivo_resultado.xlsx"

# Definir destinatarios de correo
DESTINATARIOS = [
    "jmartini@ufd.es",
    "scalvor@ufd.es",
    "imartinm@ufd.es"
]
CC = []
CCO = ["pdenisr@ufd.es"]

# Definir asunto del correo
ASUNTO_CORREO = "Datalake Comer"
FIRMA_HTML = """
<p>Firmado,<br>
Paula Denis</p>
"""
