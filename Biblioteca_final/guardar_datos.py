# codigo hecho por Jaziel Aranda :)) 
# Estas son las cosas que vamos a ocupar para que todo funcione
import csv
import os
# Estas son las listas globales, las que tienen los libros y prestamos iniciales
from libros import libros as lista_libros_global
from prestamos import prestamos as lista_prestamos_global
from colorama import Fore,Style

# estas variables tienen el nombre del archivo para que sea más fácil usarlas
ARCHIVO_LIBROS = "libros.csv"
ARCHIVO_PRESTAMOS = "prestamos.csv"


# esta funcion guarda todos los datos de libros y prestamos a sus archivos
def guardar_datos():
    
    # aqui se intenta guardar la informacion de los libros
    try:
       
        # estas son las columnas que tendra el archivo de libros
        columnas_libros = ["id", "titulo", "autor", "año", "genero", "disponible"]
        
       
        # abre el archivo 'libros.csv' en modo escritura por eso se pone la w osea write
        with open(ARCHIVO_LIBROS, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=columnas_libros)
            writer.writeheader() # esto pone los títulos de las columnas

            # recorre cada libro en la lista global de libros y escribe el libro en el archivo
            for libro in lista_libros_global:
                
                writer.writerow(libro) 
                
        
    # si algo falla al guardar los libros, esto lo detecta 
    except Exception as e:
        print(Fore.RED+Style.BRIGHT+f"Error al guardar libros en CSV: {e}"+Style.RESET_ALL)

    # ahora intenta guardar la información de los prestamos
    try:
        # estas son las columnas para el archivo de prestamos
        columnas_prestamos = ['titulo', 'nombre_prestatario', 'fecha_prestamo', 'fecha_devolucion']
        
        # abre el archivo 'prestamos.csv' en modo escritura igual por eso la w
        with open(ARCHIVO_PRESTAMOS, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=columnas_prestamos)
            writer.writeheader()
            
            # aqui va por cada prestamo en la lista global
            for prestamo in lista_prestamos_global:
                # convierte las fechas a texto si es necesario para el archivo
                writer.writerow({
                    "titulo": prestamo.get("titulo"),
                    "nombre_prestatario": prestamo.get("nombre_prestatario"),
                    "fecha_prestamo": str(prestamo.get("fecha_prestamo")),
                    "fecha_devolucion": str(prestamo.get("fecha_devolucion")) if prestamo.get("fecha_devolucion") else ""
                })
                
        print(Fore.GREEN+Style.BRIGHT+f"datos guardados correctamente en {ARCHIVO_PRESTAMOS}"+Style.RESET_ALL)
    # si algo falla al guardar prestamos, lo atrapa aqui
    except Exception as e:
        print(Fore.RED+Style.BRIGHT+f"Error al guardar préstamos en CSV: {e}"+Style.RESET_ALL)


# esta funcion lee los archivos csv y carga los datos a las listas
def cargar_datos():
    # comprueba si el archivo de libros existe
    if os.path.exists(ARCHIVO_LIBROS):
        try:
            # abre el archivo de libros para leer se pine la r de read o leer en ingles
            with open(ARCHIVO_LIBROS, mode='r', encoding='utf-8') as f:
                reader = csv.DictReader(f) # esto lee cada linea como un diccionario
                
                nuevos_libros = []
                # para cada fila o sea libro que lee...
                for row in reader:
                    # como el csv solo lee texto, aqui convertierte los tipos de datos
                    libro = {
                        "id": int(row["id"]),                  
                        "titulo": row["titulo"],
                        "autor": row["autor"],
                        "año": int(row["año"]),                 
                        "genero": row["genero"],
                        "disponible": row["disponible"] == 'True' 
                    }
                    nuevos_libros.append(libro)
                
                # si si leyo libros, borra la lista vieja y mete la info nueva
                if nuevos_libros:
                    lista_libros_global.clear()
                    lista_libros_global.extend(nuevos_libros)
                    print(f"Libros cargados: {len(nuevos_libros)}")
                    
        # si hay un error al leer el archivo
        except Exception as e:
            print(Fore.RED+Style.BRIGHT+f"Error al leer {ARCHIVO_LIBROS}: {e}"+Style.RESET_ALL)
    else:
        # si no existe el archivo
        print(f"no existe {ARCHIVO_LIBROS}, se usarán los libros por defecto.")

    # --- CARGAR PRÉSTAMOS --- 🤝
    # checa si el archivo de prestamos existe
    if os.path.exists(ARCHIVO_PRESTAMOS):
        try:
            # abre el archivo de prestamos para leer
            with open(ARCHIVO_PRESTAMOS, mode='r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                
                nuevos_prestamos = []
                # para cada fila (prestamo) que lee...
                for row in reader:
                    # como casi todo ya es texto, es mas directo
                    prestamo = {
                        "titulo": row["titulo"],
                        "nombre_prestatario": row["nombre_prestatario"],
                        "fecha_prestamo": row["fecha_prestamo"],
                        "fecha_devolucion": row["fecha_devolucion"]
                    }
                    nuevos_prestamos.append(prestamo)
                
                # actualiza la lista global de prestamos con los datos del archivo
                lista_prestamos_global.clear()
                lista_prestamos_global.extend(nuevos_prestamos)
                print(Fore.GREEN+Style.BRIGHT+f"Préstamos cargados: {len(nuevos_prestamos)}"+Style.RESET_ALL)

        # si hay un error al leer este archivo
        except Exception as e:
            print(Fore.RED+Style.BRIGHT+f"Error al leer {ARCHIVO_PRESTAMOS}: {e}"+Style.RESET_ALL)