# Datalake Comer

Este proyecto permite procesar ficheros CSV, generar un Excel con la información combinada y enviar un correo automático con el resultado.

---

1- Primero debes entrar en DL, ejecutar las consultas SGC y Zeus y descargar ambos archivos.

---

## Primeros pasos (solo la primera vez)

1. Abre la terminal y navega hasta la carpeta donde quieras guardar el proyecto.
   Por ejemplo:
	cd C:\Users\uf754247\OneDrive - NATURGY INFORMATICA S.A\mis cosas\programas\datalake_comercializadoras

2. Clona el repositorio:

   Ejecuta en la terminal:

   git clone https://github.com/PaulaDenisUFD/UFD

   Si no te funciona, puede ser que no tengas acceso. Solicítaselo a Paula.

2. Accede a la carpeta del proyecto:

   cd UFD

3. Ejecuta el archivo de configuración inicial (`setup.bat`):

   Este script creará un entorno virtual e instalará las dependencias necesarias.

   setup.bat

4. Copia el archivo de configuración:

   El archivo `configuracion_example.py` contiene un ejemplo de configuración. Cada usuario debe copiarlo y modificarlo:

   4.1 Cambia el nombre del archivo a 'configuracion.py'
   4.2 Abre configuracion.py y cambia la firma del correo.

---

## Uso diario

Una vez configurado por primera vez:

1. Activa el entorno virtual (si no está activado):

   .venv\Scripts\activate

2. Ejecuta el programa principal:

   python dlcomer.py

---

## Cómo actualizar el código

Si el proyecto se actualiza (por ejemplo, tú o alguien sube cambios al GitHub):

1. Guarda tu trabajo y asegúrate de que no tienes cambios pendientes.
2. Haz un `pull` para traer los últimos cambios:

   git pull

⚠️ **El archivo `configuracion.py` no se actualiza ni se sobrescribe**, ya que está en `.gitignore`. (Esto quiere decir, que aunque te traigas una versión nueva, no se te cambia la configuración)

Si se actualiza la estructura del archivo de configuración, se notificará con una nueva versión de `configuracion_example.py`. En ese caso, revisa y copia lo nuevo si lo necesitas.

---

## Recomendaciones

- Nunca subas tu `configuracion.py` al repositorio.
- Mantén actualizado el código con `git pull`.
- Si surgen errores, asegúrate de tener el entorno virtual activo y actualizado.

---

## 🧰 ¿No tienes Git instalado?

Si aún no tienes Git en tu ordenador, sigue estos pasos:

### 1. Instalar Git

1. Ve a la página oficial: https://git-scm.com/
2. Descarga la versión para Windows.
3. Ejecuta el instalador y deja todas las opciones por defecto.
4. Reinicia el ordenador si es necesario.

### 2. Abrir una terminal

Puedes usar:

- CMD o PowerShell de Windows (funciona también).

### 4. Configura tu nombre de usuario:

git config --global user.name "Tu Nombre"

### 5. Configura tu correo (el mismo que usas en GitHub):

git config --global user.email "tu_email@ufd.es"

### 6.  Verifica que se ha guardado bien:

git config --list


### 7. Una vez hecho esto, puedes pasar al capítulo "Primeros pasos".


