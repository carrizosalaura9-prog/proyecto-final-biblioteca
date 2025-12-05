#Código hecho por Luis Valles
from tkinter import messagebox
import tkinter as tk
import datetime
# Lista global de libros
libros = [
    # ----------- TERROR (10) -----------
    {"id": 183421,"titulo": "El monje", "autor": "Autor 1", "año": 1990, "genero": "Terror"},
    {"id": 298314,"titulo": "Casa oscura", "autor": "Autor 2", "año": 1985, "genero": "Terror"},
    {"id": 537812,"titulo": "Noche roja", "autor": "Autor 3", "año": 2001, "genero": "Terror"},
    {"id": 624551,"titulo": "El demonio", "autor": "Autor 4", "año": 1978, "genero": "Terror"},
    {"id": 731290,"titulo": "La sombra", "autor": "Autor 5", "año": 1999, "genero": "Terror"},
    {"id": 845903,"titulo": "Puerta negra", "autor": "Autor 6", "año": 2010, "genero": "Terror"},
    {"id": 952771,"titulo": "El ritual", "autor": "Autor 7", "año": 2008, "genero": "Terror"},
    {"id": 168332,"titulo": "Luz muerta", "autor": "Autor 8", "año": 1992, "genero": "Terror"},
    {"id": 279441,"titulo": "Bosque gris", "autor": "Autor 9", "año": 1995, "genero": "Terror"},
    {"id": 100000,"titulo": "Eco final", "autor": "Autor 10", "año": 2018, "genero": "Terror"},

    # ----------- AMOR (10) -----------
    {"id": 100001,"titulo": "Amor eterno", "autor": "Autor 11", "año": 2005, "genero": "Amor"},
    {"id": 100002,"titulo": "Besos dulces", "autor": "Autor 12", "año": 2012, "genero": "Amor"},
    {"id": 100003,"titulo": "Corazon rojo", "autor": "Autor 13", "año": 1999, "genero": "Amor"},
    {"id": 100004,"titulo": "Nuestro dia", "autor": "Autor 14", "año": 2017, "genero": "Amor"},
    {"id": 100005,"titulo": "Bella historia", "autor": "Autor 15", "año": 2001, "genero": "Amor"},
    {"id": 100006,"titulo": "Cita perfecta", "autor": "Autor 16", "año": 2019, "genero": "Amor"},
    {"id": 100007,"titulo": "Mi destino", "autor": "Autor 17", "año": 2003, "genero": "Amor"},
    {"id": 100008,"titulo": "Flor blanca", "autor": "Autor 18", "año": 1994, "genero": "Amor"},
    {"id": 100009,"titulo": "Dulce luna", "autor": "Autor 19", "año": 2020, "genero": "Amor"},
    {"id": 100010,"titulo": "Caminos juntos", "autor": "Autor 20", "año": 2015, "genero": "Amor"},

    # ----------- ACCION (10) -----------
    {"id": 323111,"titulo": "Furia total", "autor": "Autor 21", "año": 2002, "genero": "Accion"},
    {"id": 323112,"titulo": "Cuenta atras", "autor": "Autor 22", "año": 2010, "genero": "Accion"},
    {"id": 323113,"titulo": "Carga mortal", "autor": "Autor 23", "año": 2007, "genero": "Accion"},
    {"id": 323114,"titulo": "Linea de fuego", "autor": "Autor 24", "año": 1998, "genero": "Accion"},
    {"id": 323115,"titulo": "Zona roja", "autor": "Autor 25", "año": 2004, "genero": "Accion"},
    {"id": 323116,"titulo": "Venganza fría", "autor": "Autor 26", "año": 2013, "genero": "Accion"},
    {"id": 323117,"titulo": "Golpe final", "autor": "Autor 27", "año": 2016, "genero": "Accion"},
    {"id": 323118,"titulo": "Lucha urbana", "autor": "Autor 28", "año": 2001, "genero": "Accion"},
    {"id": 323119,"titulo": "Operacion sombra", "autor": "Autor 29", "año": 2018, "genero": "Accion"},
    {"id": 323120,"titulo": "Camino de acero", "autor": "Autor 30", "año": 1996, "genero": "Accion"},
]

# Marcar todos los libros como disponibles al inicio
for libro in libros:
    libro["disponible"] = True

prestamos = []  # lista global de préstamos


def actualizar_listbox(tabla, data):
    # Limpiar tabla
    tabla.delete(*tabla.get_children())

    # Si no hay datos
    if not data:
        return

    # Insertar filas
    for libro in data:
        tabla.insert("", "end", values=(
            libro.get("id", "N/A"),
            libro["titulo"],
            libro["autor"],
            libro["año"],
            libro["genero"]
        ))


def agregar_libro(entry_idlibro, entry_titulo, entry_autor, entry_anio, entry_genero, listbox_libros):
    
    global libros
    try:
        id1 = entry_idlibro.get().strip()
        titulo1 = entry_titulo.get().strip()
        autor1 = entry_autor.get().strip()
        anio1 = entry_anio.get().strip()
        genero1 = entry_genero.get().strip()
        
       
        if not id1 or not titulo1 or not autor1 or not anio1 or not genero1:
            messagebox.showwarning("Advertencia", "Todos los campos (incluyendo ID) son obligatorios.")
            return

        # Validar ID como número
        try:
            nuevo_id = int(id1)
        except ValueError:
            messagebox.showerror("Error", "El ID debe ser un número entero válido.")
            return

        # Validar año
        try:
            anio1 = int(anio1)
        except ValueError:
            messagebox.showerror("Error", "El año debe ser un número entero válido.")
            return
            
    except Exception as e:
        messagebox.showerror("Error de entrada", f"Error al leer los campos: {e}")
        return

   
    for libro in libros:
        if libro.get("id") == nuevo_id:
            messagebox.showwarning(
                "Duplicado",
                f"Ya existe un libro con el ID: {nuevo_id}. Use otro ID."
            )
            return

    
    for libro in libros:
        if libro["titulo"].lower() == titulo1.lower():
            messagebox.showwarning(
                "Duplicado",
                "Ya existe un libro con ese título. Se agregará si el ID es diferente."
            )
            break
    
    libro = {"id": nuevo_id, "titulo": titulo1, "autor": autor1, "año": anio1, "genero": genero1}
    libros.append(libro)
    
    

    # Limpiar campos de entrada
    entry_idlibro.delete(0, tk.END)
    entry_titulo.delete(0, tk.END)
    entry_autor.delete(0, tk.END)
    entry_anio.delete(0, tk.END)
    entry_genero.delete(0, tk.END)
    
    # Actualizar la visualización de libros
    actualizar_listbox(listbox_libros, libros)

def buscar_libro(entry_texto, listbox_libros):
    
    global libros
    texto = entry_texto.get().strip().lower()
    
    if not texto:
        # Si no hay texto, mostrar todos los libros
        actualizar_listbox(listbox_libros, libros)
        return
        
    resultados = []
    
    for libro in libros:
        # Busca por ID (como cadena), título, autor o género
        id1 = str(libro.get("id", "N/A")).lower()
        if texto in id1 or \
           texto in libro["titulo"].lower() or \
           texto in libro["autor"].lower() or \
           texto in libro["genero"].lower():
            resultados.append(libro)
            
    if not resultados:
        messagebox.showinfo("Búsqueda", f"No se encontraron libros para la búsqueda: '{texto}'.")
        
    actualizar_listbox(listbox_libros, resultados)

def eliminar_libro(entry_titulo, listbox_libros):
    global libros
    titulo_a_eliminar = entry_titulo.get().strip().lower()
    
    if not titulo_a_eliminar:
        messagebox.showwarning("Advertencia", "Debe ingresar el título del libro a eliminar.")
        return
    
   
    nueva_lista = [libro for libro in libros if libro["titulo"].lower() != titulo_a_eliminar]

    
    if len(nueva_lista) < len(libros):
        
        libros[:] = nueva_lista 
        
        entry_titulo.delete(0, tk.END)
        actualizar_listbox(listbox_libros, libros)
        messagebox.showinfo("Éxito", f"El libro '{titulo_a_eliminar}' ha sido eliminado.")
    else:
        messagebox.showwarning("Advertencia", f"No se encontró ningún libro con el título '{titulo_a_eliminar}'.")
    if len(nueva_lista) < len(libros):
        libros[:] = nueva_lista 
        
        
        from guardar_datos import guardar_datos
        guardar_datos()
        

        entry_titulo.delete(0, tk.END)
        actualizar_listbox(listbox_libros, libros)


def mostrar_librosU():
    return libros














def prestar_libro(entry_titulo, listbox_libros):
    global libros, prestamos

    titulo = entry_titulo.get().strip().lower()

    if not titulo:
        messagebox.showwarning("Advertencia", "Ingrese el título del libro a prestar.")
        return

    # Buscar libro
    for libro in libros:
        if libro["titulo"].lower() == titulo:

            if libro["disponible"] == False:
                messagebox.showerror("Error", "Este libro ya está prestado.")
                return

            # Registrar préstamo
            libro["disponible"] = False
            fecha = datetime.date.today()

            prestamos.append({
                "titulo": libro["titulo"],
                "fecha_prestamo": fecha,
                "fecha_devolucion": ""
            })

            messagebox.showinfo("Éxito", f"Libro '{libro['titulo']}' prestado correctamente.")
            actualizar_listbox(listbox_libros, libros)
            return

    messagebox.showerror("Error", "No se encontró un libro con ese título.")

def devolver_libro(entry_titulo, listbox_libros):
    global libros, prestamos

    titulo = entry_titulo.get().strip().lower()

    if not titulo:
        messagebox.showwarning("Advertencia", "Ingrese el título del libro a devolver.")
        return

    # Buscar libro
    for libro in libros:
        if libro["titulo"].lower() == titulo:

            if libro["disponible"] == True:
                messagebox.showerror("Error", "Este libro no está prestado.")
                return

            libro["disponible"] = True
            fecha = datetime.date.today()

            # Registrar fecha de devolución
            for p in prestamos:
                if p["titulo"].lower() == titulo and p["fecha_devolucion"] == "":
                    p["fecha_devolucion"] = fecha
                    break

            messagebox.showinfo("Éxito", f"Libro '{libro['titulo']}' devuelto correctamente.")
            actualizar_listbox(listbox_libros, libros)
            return

    messagebox.showerror("Error", "No existe préstamo activo para este libro.")
