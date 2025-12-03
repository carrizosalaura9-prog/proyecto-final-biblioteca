#Código hecho por Azul Morales
import tkinter as tk
from tkinter import messagebox

#asignamos el nombre del archvio con los usuarios a una variable
NOMBRE_ARCHIVO= "usuarios.txt"
usuarios = {}
ultimo_usuario_activo= None

def registrar_usuario(nombre_n_entry, id_entry, contraseña_entry,):
    try:
        #obtener los datos
        nombre_nuevo= nombre_n_entry.get()
        ID_nuevo= int(id_entry.get())
        contraseña_nueva= contraseña_entry.get()
            

        if not contraseña_nueva or not nombre_nuevo: #si dejan la contraseña vacia o el nombre
            messagebox.showerror("Error de Registro", "La contraseña no puede estar vacía.")
            return

        if ID_nuevo in usuarios: #Verifica si ID se encuentra en usuarios
          messagebox.showerror("Error de Registro", "Este ID ya está registrado, intente con otro.")
        else:
           usuarios[ID_nuevo] = {"nombre": nombre_nuevo, "contraseña": contraseña_nueva} #meter los datos en usuarios
           
            # Modo 'a' (append/anexar): crea el archivo si no existe y escribe al final si ya existe.
        with open(NOMBRE_ARCHIVO, 'a', encoding='utf-8') as f:
            contenido = f"{ID_nuevo},{nombre_nuevo},{contraseña_nueva}"
            f.write(contenido + "\n")

           #limpiar todo, desde el inicio (0)
        id_entry.delete(0, tk.END)
        contraseña_entry.delete(0, tk.END)
        nombre_n_entry.delete(0, tk.END)

    except ValueError: #Si el ID no es puesto en numeros
        messagebox.showerror("Error de ID", "El ID debe ser un número entero.")

    


def iniciar_sesion(id_entry, contraseña_entry, ver_ultimo_usuario_label_widget):
  global ultimo_usuario_activo #modifica el valor cada vez que se inicie sesion
  try:
        #obtener los datos
        ID= int(id_entry.get())
        contraseña= contraseña_entry.get()

        if ID not in usuarios: #ID no registrado
            messagebox.showerror("Error de Inicio", "El usuario no está registrado.")
            return
        
        contraseña_guardada= usuarios[ID]["contraseña"] #acceder el dato

        if contraseña_guardada!= contraseña: 
          messagebox.showerror("Error de inicio de sesion", "Los datos son incorrectos.")
        else:
           nombre_guardado= usuarios[ID]["nombre"]        
           ultimo_usuario_activo= ID #guarda el ultimo usuario (ID)
           ultimo_usuario= f"Bienvenido {nombre_guardado}"
           ver_ultimo_usuario_label_widget.config(text=ultimo_usuario,font="Verdana 10 bold", fg="#FFFFFF")
           

           #limpiar todo, desde el inicio (0)
           id_entry.delete(0, tk.END)
           contraseña_entry.delete(0, tk.END)

  except ValueError: #Si el ID no es puesto en numeros
        messagebox.showerror("Error de ID", "El ID debe ser un número entero.")