# importo librerias
import pandas as pd
import os
from pathlib import Path
from datetime import datetime
import win32com.client
import json
from configuracion import *


# Función para eliminar archivos en un directorio
def eliminar_archivos(directorio):
    archivos = list(directorio.glob('*'))  # Obtener todos los archivos en el directorio
    for archivo in archivos:
        if archivo.is_file():  # Verificar que realmente es un archivo
            print(f"Eliminando archivo: {archivo}")
            archivo.unlink()  # Eliminar el archivo

def get_latest_downloaded_file(directory_path):
    # print(directory_path)
    # print(directory_path.exists())
    # print(directory_path.is_dir())

    # Check if the directory exists
    if directory_path.exists() and directory_path.is_dir():
        # Get a list of all files in the directory
        files = directory_path.glob('*.csv')

        # Filter out directories from the list
        files = [file for file in files if file.is_file()]

        # Sort the files by modification time in descending order
        files.sort(key=lambda x: os.path.getmtime(x), reverse=True)

        # Get the latest file, if any
        if files:
            latest_file = files[0]
            second_file = files[1]
            return latest_file, second_file
        else:
            return "No files found in the directory."
    else:
        return "Directory does not exist or is not a directory."


def enviar_correo(destinatario,cc,cco, asunto, ruta_archivo):
    outlook = win32com.client.Dispatch('Outlook.Application')
    correo = outlook.CreateItem(0)
    correo.To = ';'.join(destinatario)
    if cc:
            correo.CC = ';'.join(cc)
    if cco:
            correo.BCC = ';'.join(cco)
    correo.Subject = asunto


    # Añadir el archivo adjunto
    correo.Attachments.Add(str(ruta_archivo))
    
    cuerpo_correo = f"""
        <html>
        <body>
        <p>Buenos días,</p>
        <p>Adjunto la extracción de esta semana<p>
        {FIRMA_HTML}
        </body>
        </html>
        """
    correo.HTMLBody = cuerpo_correo
    correo.Send()






def dividir_si_numero(valor):
    try:
        # Intentamos convertir el valor a número (float)
        if type(valor) != str:
            return valor / 1000  # Si es un número, lo dividimos
        else:
            return float(valor)
    except ValueError:
        # Si no se puede convertir a número, es una cadena o valor no numérico, lo dejamos igual
        return valor


# Leer el archivo CSV
def cargar_csv_a_pandas(ar1,ar2, ruta_fin):

        df1 = pd.read_csv(ar1)
        print(f"Archivo '{ar1.name}' leído con éxito.")
        df2 = pd.read_csv(ar2)
        print(f"Archivo '{ar2.name}' leído con éxito.")

        # Asegurarnos de que las columnas sean las mismas
        if list(df1.columns) == list(df2.columns):
            # Unir ambos DataFrames por filas
            df_combinado = pd.concat([df1, df2], ignore_index=True)
        else:
            raise ValueError("Las columnas de los archivos no coinciden")
        # Concatenar los dos DataFrames
        df_combinado = pd.concat([df1, df2], ignore_index=True)  

        df_combinado[df_combinado.columns[0]] = pd.to_datetime(df_combinado[df_combinado.columns[0]], errors='coerce')

        # Eliminar la hora y quedarnos solo con la fecha
        df_combinado[df_combinado.columns[0]] = df_combinado[df_combinado.columns[0]].dt.date 
        
        # Ordenar el DataFrame por la primera columna (fecha) de más reciente a más antiguo
        df_combinado = df_combinado.sort_values(by=[df_combinado.columns[1], df_combinado.columns[0]], ascending=[False, False]) 

        # cambiar el la columna cups 

        df_combinado['cups'] = df_combinado['cups'].apply(lambda x: x[:21] + "F")


        df_combinado.rename(columns={'potencia contratada': 'potencia contratada KW'}, inplace=True)
        df_combinado['potencia contratada KW'] = df_combinado['potencia contratada KW'].apply(dividir_si_numero)

        columna_excluir = "fecha datos"
        
        # Crear un DataFrame sin la columna 'fecha datos' solo para comparar duplicados
        df_sin_fecha = df_combinado.drop(columns=[columna_excluir])

        # Identificar duplicados sin considerar 'fecha datos'
        duplicados = df_sin_fecha.duplicated(keep=False)

        # Filtrar el DataFrame eliminando todas las filas duplicadas
        df_combinado = df_combinado[~duplicados]


        # Obtener la fecha de hoy en formato YYYY-MM-DD
        fecha_hoy = datetime.now().strftime("%d-%m-%Y")
        nombre_archivo_salida = f"datalake_comer_{fecha_hoy}.xlsx"

        ruta_final = ruta_fin / nombre_archivo_salida

        # Guardar el resultado en un archivo Excel
        df_combinado.to_excel(ruta_final, index=False)

        print(f"Archivos combinados y guardados como '{nombre_archivo_salida}'")


        return ruta_final
    



def main():

    eliminar_archivos(RUTA_ENTRADA)
    eliminar_archivos(RUTA_SALIDA)
    latest_file, second_file = get_latest_downloaded_file(RUTA_DESCARGAS)

    ar1 = RUTA_ENTRADA / latest_file.name
    ar2 = RUTA_ENTRADA / second_file.name

    latest_file.rename(ar1)
    second_file.rename(ar2)

    print(ar1)
    print(ar2)


    archivo_envio = cargar_csv_a_pandas(ar1,ar2, RUTA_SALIDA)

    # path_envio = Path(r'C:\Users\uf754247\OneDrive - NATURGY INFORMATICA S.A\mis cosas\programas\datalake_comer\output')
    path_envio = RUTA_SALIDA
    path_envio = path_envio / archivo_envio.name


    asunto = f'Datalake Comer'

    # enviar_correo(DESTINATARIOS, CC, CCO, asunto, path_envio)
    

main()

