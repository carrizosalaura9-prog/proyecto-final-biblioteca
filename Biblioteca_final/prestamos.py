
from tkinter import messagebox
from datetime import date
from libros import libros
import tkinter as tk 



prestamos = [] 

def obtener_prestados():
    
    return prestamos

def actualizar_listbox_prestamos(tabla, data):
    
    tabla.delete(*tabla.get_children())

    
    if not data:
        return

    
    for prestamo in data:
        
        tabla.insert("", "end", values=(
            prestamo["titulo"],
            prestamo["nombre_prestatario"],
            prestamo["fecha_prestamo"]
        ))
        
def actualizar_combobox_libros(combobox, lista_libros):
    
    libros_disponibles_titulos = []
    
    for libro in lista_libros:
        
        if libro.get("disponible", True): 
            libros_disponibles_titulos.append(libro["titulo"])
            
    combobox['values'] = libros_disponibles_titulos
    
  
    if libros_disponibles_titulos:
        combobox.set(libros_disponibles_titulos[0])
    else:
        combobox.set("No hay libros disponibles")


def prestar_libro(combobox_libro, entry_nombre_prestatario, listbox_prestamos):
  
    global libros, prestamos
   
    titulo_a_prestar = combobox_libro.get().strip()
    nombre_prestatario = entry_nombre_prestatario.get().strip()
    
    if not titulo_a_prestar or titulo_a_prestar == "No hay libros disponibles":
        messagebox.showwarning("Advertencia", "Seleccione un libro para prestar.")
        return

    if not nombre_prestatario:
        messagebox.showwarning("Advertencia", "Ingrese el nombre del prestatario (usuario).")
        return
        
    
    libro_encontrado = None
    for libro in libros:
        if libro["titulo"] == titulo_a_prestar and libro.get("disponible", True):
            libro["disponible"] = False 
            libro_encontrado = libro
            break

    if not libro_encontrado:
       
        messagebox.showerror("Error", f"El libro '{titulo_a_prestar}' no está disponible o no existe.")
        return

    
    fecha_prestamo = date.today()
    
    prestamos.append({
        "titulo": libro_encontrado["titulo"],
        "nombre_prestatario": nombre_prestatario, 
        "fecha_prestamo": str(fecha_prestamo),
        "fecha_devolucion": ""
    })
    

    try:
        from guardar_datos import guardar_datos
        guardar_datos()
    except ImportError:
        pass 
    entry_nombre_prestatario.delete(0, tk.END)
    
    actualizar_listbox_prestamos(listbox_prestamos, prestamos)
    actualizar_combobox_libros(combobox_libro, libros) 
    

def devolver_libro(entry_titulo, listbox_prestamos, combobox_libro):
    
    global libros, prestamos
    
    titulo_a_devolver = entry_titulo.get().strip()

    if not titulo_a_devolver:
        messagebox.showwarning("Advertencia", "Debe ingresar el título del libro a devolver.")
        return

    
    prestamo_encontrado = None
    indice_prestamo = -1
    
    for i, prestamo in enumerate(prestamos):
        
        if prestamo["titulo"].lower() == titulo_a_devolver.lower():
            prestamo_encontrado = prestamo
            indice_prestamo = i
            break
            
    if not prestamo_encontrado:
        messagebox.showwarning("Advertencia", f"El libro '{titulo_a_devolver}' no se encuentra registrado como prestado.")
        return

    
    libro_devuelto = False
    for libro in libros:
        if libro["titulo"].lower() == titulo_a_devolver.lower():
            libro["disponible"] = True
            libro_devuelto = True
            break
            
    if not libro_devuelto:
        
        messagebox.showerror("Error Interno", f"El libro '{titulo_a_devolver}' no se encontró en el catálogo principal al intentar devolverlo.")
        return

    
    
    prestamos.pop(indice_prestamo)
    
    
    
    entry_titulo.delete(0, tk.END)
    actualizar_listbox_prestamos(listbox_prestamos, prestamos)
    actualizar_combobox_libros(combobox_libro, libros)