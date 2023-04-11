import tkinter as tk
from tkinter import filedialog
import os

# Creamos la ventana principal de la aplicación
ventana = tk.Tk()
ventana.title("Buscador de archivos")
ventana.geometry("400x200")
ventana.configure(bg='#2B2B2B')

# Etiqueta para indicar al usuario que seleccione un archivo
etiqueta_archivo = tk.Label(ventana, text="Seleccione un archivo:", font=("Arial", 14), fg="#FFFFFF", bg='#2B2B2B')
etiqueta_archivo.pack(pady=10)

# Función que se ejecuta al hacer clic en el botón "Buscar archivo"
def buscar_archivo():
    ruta_archivo = filedialog.askopenfilename()
    if ruta_archivo:
        etiqueta_resultado.config(text="El archivo seleccionado es:\n{}".format(ruta_archivo), fg="#FFFFFF")
        boton_abrir.config(state=tk.NORMAL)
    else:
        etiqueta_resultado.config(text="No se seleccionó ningún archivo.", fg="#FFFFFF")
        boton_abrir.config(state=tk.DISABLED)

# Botón para buscar el archivo
boton_buscar = tk.Button(ventana, text="Buscar archivo", command=buscar_archivo, bg="#FF4136", fg="#FFFFFF", font=("Arial", 14, "bold"))
boton_buscar.pack(pady=10)

# Etiqueta para mostrar el resultado de la búsqueda
etiqueta_resultado = tk.Label(ventana, text="", font=("Arial", 14), bg='#2B2B2B')
etiqueta_resultado.pack(pady=10)

# Función que se ejecuta al hacer clic en el botón "Abrir archivo"
def abrir_archivo():
    ruta_archivo = etiqueta_resultado.cget("text").split("\n")[1]
    os.startfile(ruta_archivo)

# Botón para abrir el archivo
boton_abrir = tk.Button(ventana, text="Abrir archivo", command=abrir_archivo, bg="#0074D9", fg="#FFFFFF", font=("Arial", 14, "bold"), state=tk.DISABLED)
boton_abrir.pack(pady=10)

# Ejecutamos el bucle principal de la aplicación
ventana.mainloop()
