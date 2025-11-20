import tkinter as tk
from tkinter import ttk
import BuscarID
from BuscarID import Encontrar_ID
#esto es un simulacro, no quedara de esta forma, editalo libremente
#creo la ventana principal
root = tk.Tk()
root.title("INSTITUTO TECNOLOGICO DE SONORA")
root.geometry("600x400")

#creo el nombre de itson, anchor anclaje de justificacion
etiqueta_itson = ttk.Label(root,text="ITSON",font="Helvica 40",foreground="#f2f2f2",background="#210fea",anchor="center" )
etiqueta_itson.pack(padx=0,fill="x")

#creo otra etiqueta que pida el ID
etiqueta_ID = ttk.Label(root,text="ID: ",font="Helvica 20",foreground="#f2f2f2",background="#210fea")
etiqueta_ID.pack(pady=10)

#creo una entrada de ID
entrada_ID = ttk.Entry(root,font="Helvica 20")
entrada_ID.pack(pady=10,padx=15)

#boton para validar ID existente
boton_ID = ttk.Button(root,text="Buscar ID",command=Encontrar_ID)
boton_ID.pack(pady=10,padx=20)



root.mainloop()