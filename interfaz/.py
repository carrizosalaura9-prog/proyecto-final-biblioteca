import tkinter as tk
from tkinter import messagebox



libros = [

    # ----------- TERROR (10) -----------
    {"id": 183421, "titulo": "El monje", "autor": "Autor", "año": 1990, "genero": "Terror"},
    {"id": 298314, "titulo": "Casa oscura", "autor": "Autor", "año": 1985, "genero": "Terror"},
    {"id": 537812, "titulo": "Noche roja", "autor": "Autor", "año": 2001, "genero": "Terror"},
    {"id": 624551, "titulo": "El demonio", "autor": "Autor", "año": 1978, "genero": "Terror"},
    {"id": 731290, "titulo": "La sombra", "autor": "Autor", "año": 1999, "genero": "Terror"},
    {"id": 845903, "titulo": "Puerta negra", "autor": "Autor", "año": 2010, "genero": "Terror"},
    {"id": 952771, "titulo": "El ritual", "autor": "Autor", "año": 2008, "genero": "Terror"},
    {"id": 168332, "titulo": "Luz muerta", "autor": "Autor", "año": 1992, "genero": "Terror"},
    {"id": 279441, "titulo": "Bosque gris", "autor": "Autor", "año": 1995, "genero": "Terror"},
    {"id": 192931, "titulo": "Eco final", "autor": "Autor", "año": 2018, "genero": "Terror"},


    # ----------- AMOR (10) -----------
    {"id": 192933, "titulo": "Amor eterno", "autor": "Autor", "año": 2005, "genero": "Amor"},
    {"id": 192934, "titulo": "Besos dulces", "autor": "Autor", "año": 2012, "genero": "Amor"},
    {"id": 192935, "titulo": "Corazon rojo", "autor": "Autor", "año": 1999, "genero": "Amor"},
    {"id": 192936, "titulo": "Nuestro dia", "autor": "Autor", "año": 2017, "genero": "Amor"},
    {"id": 192937, "titulo": "Bella historia", "autor": "Autor", "año": 2001, "genero": "Amor"},
    {"id": 192938, "titulo": "Cita perfecta", "autor": "Autor", "año": 2019, "genero": "Amor"},
    {"id": 192939, "titulo": "Mi destino", "autor": "Autor", "año": 2003, "genero": "Amor"},
    {"id": 192940, "titulo": "Flor blanca", "autor": "Autor", "año": 1994, "genero": "Amor"},
    {"id": 192941, "titulo": "Dulce luna", "autor": "Autor", "año": 2020, "genero": "Amor"},
    {"id": 192942, "titulo": "Caminos juntos", "autor": "Autor", "año": 2015, "genero": "Amor"},


    # ----------- ACCION (10) -----------
    {"id": 323111, "titulo": "Furia total", "autor": "Autor", "año": 2002, "genero": "Accion"},
    {"id": 323112, "titulo": "Cuenta atras", "autor": "Autor", "año": 2010, "genero": "Accion"},
    {"id": 323113, "titulo": "Carga mortal", "autor": "Autor", "año": 2007, "genero": "Accion"},
    {"id": 323114, "titulo": "Linea de fuego", "autor": "Autor", "año": 1998, "genero": "Accion"},
    {"id": 323115, "titulo": "Zona roja", "autor": "Autor", "año": 2004, "genero": "Accion"},
    {"id": 323116, "titulo": "Venganza fría", "autor": "Autor", "año": 2013, "genero": "Accion"},
    {"id": 323117, "titulo": "Golpe final", "autor": "Autor", "año": 2016, "genero": "Accion"},
    {"id": 323118, "titulo": "Lucha urbana", "autor": "Autor", "año": 2001, "genero": "Accion"},
    {"id": 323119, "titulo": "Operacion sombra", "autor": "Autor", "año": 2018, "genero": "Accion"},
    {"id": 323120, "titulo": "Camino de acero", "autor": "Autor", "año": 1996, "genero": "Accion"},

]

#Agregar libros
def agregar_libro(idlibro, titulo, autor, anio, genero,):
    global libros
    try:
        id_val = idlibro.get().strip()
        titulo_val = titulo.get().strip()
        autor_val = autor.get().strip()
        anio_val = anio.get().strip()
        genero_val = genero.get().strip()
    except ValueError:
        messagebox.showerror("Error", "El año debe ser un numero entero")
        return
    #Libro ya existente
    for libro in libros:
        if libro["titulo"].lower() == titulo_val.lower():
            messagebox.showwarning(
                "Duplicado",
                "Ya existe un libro con ese título."
            )
            return

    libro = {"id": id_val, "titulo": titulo_val, "autor": autor_val, "año": anio_val, "genero": genero_val}
    libros.append(libro)

    
    #Eliminar los datos al agregar un libro
    idlibro.delete(0, tk.END)
    titulo.delete(0, tk.END)
    autor.delete(0, tk.END)
    anio.delete(0, tk.END)
    genero.delete(0, tk.END)
    actualizar_lista()
    return


#Eliminar libro
def eliminar_libro():
    titulo_eliminar = eliminar_libro2.get().strip()

    # Buscar el libro por su título dentro de los diccionarios
    libro_encontrado = None
    for libro in libros:
        if libro["titulo"].lower() == titulo_eliminar.lower():
            libro_encontrado = libro
            break
    #Eliminar libro y llama a la funcion para actualizar la lista
    if libro_encontrado:
        libros.remove(libro_encontrado)
        actualizar_lista()



#Actualizar lista de libros
def actualizar_lista():
    # Limpiar el Listbox y actualizarlo con los libros restantes
    lista_libros.delete(0, tk.END)
    for libro in libros:
        lista_libros.insert(tk.END, libro)

ventana = tk.Tk()
ventana.title("Libros")

label = tk.Label(ventana, text="AGREGAR UN LIBRO.")
label.pack(padx=5)

label = tk.Label(ventana, text="ID")
label.pack(padx=5)

id = tk.Entry(ventana, width=40)
id.pack(pady=5)

label = tk.Label(ventana, text="Titulo")
label.pack(padx=5)

titulo = tk.Entry(ventana, width=40)
titulo.pack(pady=5)

label = tk.Label(ventana, text="Autor")
label.pack(padx=5)

autor = tk.Entry(ventana, width=40)
autor.pack(pady=5)

label = tk.Label(ventana, text="Año")
label.pack(padx=5)

anio = tk.Entry(ventana, width=40)
anio.pack(pady=5)

label = tk.Label(ventana, text="Genero")
label.pack(padx=5)

genero = tk.Entry(ventana, width=40)
genero.pack(pady=5)

btn_agregar = tk.Button(ventana, text="Agregar libro", command=lambda: agregar_libro(id, titulo, autor, anio, genero), bg="#45DE28")
btn_agregar.pack(pady=5)

label = tk.Label(ventana, text="ELIMINAR UN LIBRO.",)
label.pack(pady=5)

eliminar_libro2 = tk.Entry(ventana, width=40)
eliminar_libro2.pack(pady=5)


btn_eliminar2 = tk.Button(ventana, text="Eliminar libro", command=eliminar_libro, bg="#F54927")
btn_eliminar2.pack(pady=5)



label_lista = tk.Label(ventana, text="Libros en el sistema")
label_lista.pack()

lista_libros = tk.Listbox(ventana, width=100, height=30)
lista_libros.pack(pady=10)

actualizar_lista()

ventana.mainloop()

