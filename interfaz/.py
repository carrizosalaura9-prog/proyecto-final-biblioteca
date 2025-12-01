import tkinter as tk
from tkinter import messagebox



libros = [

    # ----------- TERROR (10) -----------
    {"titulo": "El monje", "autor": "Autor 1", "año": 1990, "genero": "Terror"},
    {"titulo": "Casa oscura", "autor": "Autor 2", "año": 1985, "genero": "Terror"},
    {"titulo": "Noche roja", "autor": "Autor 3", "año": 2001, "genero": "Terror"},
    {"titulo": "El demonio", "autor": "Autor 4", "año": 1978, "genero": "Terror"},
    {"titulo": "La sombra", "autor": "Autor 5", "año": 1999, "genero": "Terror"},
    {"titulo": "Puerta negra", "autor": "Autor 6", "año": 2010, "genero": "Terror"},
    {"titulo": "El ritual", "autor": "Autor 7", "año": 2008, "genero": "Terror"},
    {"titulo": "Luz muerta", "autor": "Autor 8", "año": 1992, "genero": "Terror"},
    {"titulo": "Bosque gris", "autor": "Autor 9", "año": 1995, "genero": "Terror"},
    {"titulo": "Eco final", "autor": "Autor 10", "año": 2018, "genero": "Terror"},

    # ----------- AMOR (10) -----------
    {"titulo": "Amor eterno", "autor": "Autor 11", "año": 2005, "genero": "Amor"},
    {"titulo": "Besos dulces", "autor": "Autor 12", "año": 2012, "genero": "Amor"},
    {"titulo": "Corazon rojo", "autor": "Autor 13", "año": 1999, "genero": "Amor"},
    {"titulo": "Nuestro dia", "autor": "Autor 14", "año": 2017, "genero": "Amor"},
    {"titulo": "Bella historia", "autor": "Autor 15", "año": 2001, "genero": "Amor"},
    {"titulo": "Cita perfecta", "autor": "Autor 16", "año": 2019, "genero": "Amor"},
    {"titulo": "Mi destino", "autor": "Autor 17", "año": 2003, "genero": "Amor"},
    {"titulo": "Flor blanca", "autor": "Autor 18", "año": 1994, "genero": "Amor"},
    {"titulo": "Dulce luna", "autor": "Autor 19", "año": 2020, "genero": "Amor"},
    {"titulo": "Caminos juntos", "autor": "Autor 20", "año": 2015, "genero": "Amor"},

    # ----------- ACCION (10) -----------
    {"titulo": "Furia total", "autor": "Autor 21", "año": 2002, "genero": "Accion"},
    {"titulo": "Cuenta atras", "autor": "Autor 22", "año": 2010, "genero": "Accion"},
    {"titulo": "Carga mortal", "autor": "Autor 23", "año": 2007, "genero": "Accion"},
    {"titulo": "Linea de fuego", "autor": "Autor 24", "año": 1998, "genero": "Accion"},
    {"titulo": "Zona roja", "autor": "Autor 25", "año": 2004, "genero": "Accion"},
    {"titulo": "Venganza fría", "autor": "Autor 26", "año": 2013, "genero": "Accion"},
    {"titulo": "Golpe final", "autor": "Autor 27", "año": 2016, "genero": "Accion"},
    {"titulo": "Lucha urbana", "autor": "Autor 28", "año": 2001, "genero": "Accion"},
    {"titulo": "Operacion sombra", "autor": "Autor 29", "año": 2018, "genero": "Accion"},
    {"titulo": "Camino de acero", "autor": "Autor 30", "año": 1996, "genero": "Accion"},
]


def agregar_libro(titulo, autor, año, genero, entry_titulo, entry_autor, entry_año, entry_genero):
    try:
        año = int(año)
    except ValueError:
        messagebox.showerror("Error", "El año debe ser un numero entero")
        return

    for libro in libros:
        if libro["titulo"].lower() == titulo.lower():
            messagebox.showwarning(
                "Duplicado",
                "Ya existe un libro con ese título."
            )
            return

    libro = {"titulo": titulo, "autor": autor, "año": año, "genero": genero}
    libros.append(libro)
    messagebox.showinfo("Accion exitosa", "El libro se agrego correctamente")
    return

entry_titulo.titulo(0, tk.END)
entry_titulo.autor(0, tk.END)
entry_titulo.año(0, tk.END)
entry_titulo.genero(0, tk.END)

def buscar_libro(texto):
    resultados = []
    for libro in libros:
        if texto.lower() in libro["titulo"].lower() or \
           texto.lower() in libro["autor"].lower() or \
           texto.lower() in libro["genero"].lower():
            resultados.append(libro)
    return resultados

def eliminar_libro(titulo):
    global libros
    nueva = []
    eliminado = False

    for libro in libros:
        if libro["titulo"].lower() == titulo.lower():
            eliminado = True
        else:
            nueva.append(libro)

    libros = nueva

    if eliminado:
        messagebox.showinfo("Eliminado", "Libro eliminado correctamente")
    else:
        messagebox.showerror("No encontrado", "No se encontró ningún libro con ese título")



def mostrar_librosU():
    return libros
