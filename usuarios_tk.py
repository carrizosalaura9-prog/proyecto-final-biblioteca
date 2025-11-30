import tkinter as tk
from tkinter import messagebox

usuarios={}

def registrar_usuario(id_entry, contraseña_entry,):
    try:
        #obtener los datos
        ID_nuevo= int(id_entry.get())
        contraseña_nueva= contraseña_entry.get()

        if not contraseña_nueva: #si dejan la contraseña vacia 
            messagebox.showerror("Error de Registro", "La contraseña no puede estar vacía.")
            return

        if ID_nuevo in usuarios: #Verifica si ID se encuentra en usuarios
          messagebox.showerror("Error de Registro", "Este ID ya está registrado, intente con otro.")
        else:
           usuarios[ID_nuevo] = contraseña_nueva #meter los datos en usuarios
           messagebox.showinfo("Registro Exitoso", f"El usuario {ID_nuevo} se ha registrado con éxito.")

    except ValueError: #Si el ID no es puesto en numeros
        messagebox.showerror("Error de ID", "El ID debe ser un número entero.")


def iniciar_sesion(id_entry, contraseña_entry):
  try:
        #obtener los datos
        ID= int(id_entry.get())
        contraseña= contraseña_entry.get()

        if ID not in usuarios: #ID no registrado
            messagebox.showerror("Error de Inicio", "El usuario no está registrado.")
            return

        if usuarios[ID] != contraseña: #Verificar si ID y contraseña puestos estan iguales en usuarios 
          messagebox.showerror("Error de inicio de sesion", "Los datos son incorrectos.")
        else:        
           messagebox.showinfo("Inicio de sesion Exitoso", f"Bienvenido {ID} :)")

  except ValueError: #Si el ID no es puesto en numeros
        messagebox.showerror("Error de ID", "El ID debe ser un número entero.")

