#este código fue hecho por mi, Jaziel Aranda :)),  aqui solo hay interfaces 
#son las importaciones que utilice de los demas documentos en main
import tkinter as tk
from datetime import datetime
from tkinter import ttk
from usuarios import registrar_usuario, iniciar_sesion
from libros import agregar_libro, buscar_libro, eliminar_libro, actualizar_listbox, libros
from guardar_datos import cargar_datos, guardar_datos
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import graficas

from prestamos import prestar_libro, devolver_libro, obtener_prestados, actualizar_listbox_prestamos, actualizar_combobox_libros 
menu_lateral = None

#esta funcion es la que puse para que al presionar el boton de salir y guardar guarde los datos
def cerrar_aplicacion():
   
    guardar_datos()
    root.destroy()

    
#Centrar la ventana de tkinter funcion que nos enseño el maestro
def centrar_ventana(ventana,ancho,alto):
    
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto = ventana.winfo_screenheight()
    x = int((pantalla_ancho/2) - (ancho/2))
    y = int((pantalla_alto/2) - (alto/2))
    return ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

#para mostrar u ocultar el menú lateral igual nos la enseño el maestro
def Mostrar_Ocultar_panel():
    
    global menu_lateral
    
    if menu_lateral.winfo_ismapped():
        # Si está visible se oculta
        menu_lateral.pack_forget()
    else:
        # Si está oculto se muwstra
        menu_lateral.pack(side=tk.LEFT, fill="y")

#Para mostrar la fecha y hora en la interfaz,
def actualizar_hora():
    
    global etiqueta_hora
    ahora = datetime.now()
    hora_actual = ahora.hour

    # Aquí se da formato a la fecha se muestra primero el dia de la semana, luego el dia del mes, luego el mes y por ultimo el año
    formato_fecha = ahora.strftime("%A, %d de %B de %Y") 
    # aquí se da formato a la hora para que sea por hora minutos y segundos
    formato_hora = ahora.strftime("%H:%M:%S")

    #Con esto se puede saber que se pondra en la interfaz dependiendo de la hora
    if 5 <= hora_actual < 12:
        saludo = "Buenos días"
    elif 12 <= hora_actual < 19:
        saludo = "Buenas tardes"
    else:
        saludo = "Buenas noches"

    # Aquí se actualiza la etiqueta y le puse las variables anteriores
    etiqueta_hora.config(text=f"""{saludo}
{formato_fecha}    {formato_hora}""", font="Verdana 8 bold")
    
    # Se actualiza cada segundo la ventana principal se pone el mil ya que se pone en milisegundos, para que vaya mostrando la hora
    root.after(1000, actualizar_hora)

#esto sirve para que al pasar el mouse el color del boton cambie, igual nos lo enseño el maestro
def pasar_mouse(e):
    
    e.widget['background'] = "#0C4F73" 

#esto es para que cuando el mouse ya no este en el boton vuelva al color original
def quitar_mouse(e):
    e.widget['background'] ="#073650"

#Ventana más información es donde puse nuestros datos, en todas las ventanas tiene la misma estructura con una barra superior un boton de salir y un titulo y ya cada una tiene distintos botones y funciones
def mas_informacion():
    
    ventana_nueva_informacion= tk.Toplevel(root)
    ventana_nueva_informacion.title("Información")
    centrar_ventana(ventana_nueva_informacion,400,400)

    barra_superior_informacion = tk.Frame(ventana_nueva_informacion,height=50,background="#052B3F")
    barra_superior_informacion.pack(side="top",fill="x")

    boton_salir_informacion = tk.Button(barra_superior_informacion, text="Salir", font="Verdana 10",foreground="#ffffff", background="#960A0A", borderwidth=0, command=ventana_nueva_informacion.destroy)
    boton_salir_informacion.pack(padx=10, pady=10, side="right")

    etiqueta_titulo = tk.Label(barra_superior_informacion, text="Autores", font="Verdana 15 bold",foreground="#ffffff",background="#052B3F")
    etiqueta_titulo.pack(padx=10, pady=10, side="left")

    panel_principal_informacion = tk.Frame(ventana_nueva_informacion,background="#C7D3EE")
    panel_principal_informacion.pack(expand=True, fill="both")

    #Aqui puse nuestros datos
    etiqueta_Nombres = tk.Label(panel_principal_informacion, text="""Aranda Carreras Jaziel Josue 00000279565
Carrizosa Lopez Laura Fernanda 00000280617
Morales Ruelas Azul Marely 00000280105
Valles Encinas Luis Angel 00000280011
Valverde Moreno Hessel Humberto 00000284143""", font="Verdana 10 ",foreground="#000000",background="#C7D3EE", justify="left")
    etiqueta_Nombres.pack(side="top", padx=20, pady=20)


#Ventana de prestamos
def crear_interfaz_prestamos():
    
    ventana_prestamos = tk.Toplevel(root)
    ventana_prestamos.title("Préstamos")
    centrar_ventana(ventana_prestamos, 800, 600)

    
    barra_superior_prestamos = tk.Frame(ventana_prestamos, background="#052B3F")
    barra_superior_prestamos.pack(fill="x")

    boton_salir_prestamos = tk.Button(barra_superior_prestamos, text="Salir", font="Verdana 10", foreground="#ffffff", background="#960A0A", borderwidth=0, command=lambda:(guardar_datos(),ventana_prestamos.destroy()))
    boton_salir_prestamos.pack(padx=10, pady=10, side="right")

    etiqueta_titulo_prestamos = tk.Label(barra_superior_prestamos, text="Gestión de Préstamos", font="Verdana 15 bold", foreground="#ffffff", background="#052B3F")
    etiqueta_titulo_prestamos.pack(padx=10, pady=10, side="left")
    
    
    panel_principal_prestamos = tk.Frame(ventana_prestamos, background="#C7D3EE", padx=10, pady=10)
    panel_principal_prestamos.pack(expand=True, fill="both")
    
    panel_formularios_prestamos = tk.Frame(panel_principal_prestamos, bg="#C7D3EE", width=300)
    panel_formularios_prestamos.pack(side="left", fill="y", padx=10, pady=10)
    
    panel_lista_prestamos = tk.Frame(panel_principal_prestamos, bg="#C7D3EE")
    panel_lista_prestamos.pack(side="right", expand=True, fill="both", padx=10, pady=10)

    
    # Aqui cree la tabla para que los libros prestados se muestren
    tabla_prestamos = ttk.Treeview(panel_lista_prestamos, columns=("Titulo", "Nombre_Prestatario", "Fecha_Prestamo"), show="headings")

    # aqui se hacen los encabezados asignandoles un nombre
    tabla_prestamos.heading("Titulo", text="Título del Libro")
    tabla_prestamos.heading("Nombre_Prestatario", text="Nombre del Prestatario") 
    tabla_prestamos.heading("Fecha_Prestamo", text="Fecha de Préstamo")

    # Esto es para definir el ancho de las columnas
    tabla_prestamos.column("Titulo", width=200, anchor=tk.CENTER)
    tabla_prestamos.column("Nombre_Prestatario", width=150, anchor=tk.CENTER) 
    tabla_prestamos.column("Fecha_Prestamo", width=150, anchor=tk.CENTER)

    #aqui ya lo pongo o enpaqueto en la interfaz
    tabla_prestamos.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

    
   #aqui se ponen mas etiquetas igual utilize anchor para que el texto se ponga a la izquierda con west o w
    tk.Label(panel_formularios_prestamos, text="PRESTAR LIBRO", font="Verdana 12 bold", fg="#073650", bg="#C7D3EE").pack(side="top", anchor="w", pady=(20, 5))
    tk.Label(panel_formularios_prestamos, text="Seleccionar Libro:", font="Verdana 10 bold", background="#C7D3EE").pack(side="top", anchor="w", pady=(10, 0))
    
    #aqui cree el combo box que basicamente es una lista desplegable donde estan los libros que se vayan prestando, el read only es para que no se puedan modificar los datos
    combobox_libro_prestar = ttk.Combobox(panel_formularios_prestamos, width=30, state="readonly")
    combobox_libro_prestar.pack(side="top", anchor="w", pady=(0, 10))

    
    tk.Label(panel_formularios_prestamos, text="Nombre de la persona a prestar:", font="Verdana 10 bold", background="#C7D3EE").pack(side="top", anchor="w", pady=(10, 0))
    entry_nombre_prestatario = tk.Entry(panel_formularios_prestamos, width=30)
    entry_nombre_prestatario.pack(side="top", anchor="w", pady=(0, 10))
    
    #aqui pongo un boton y se usa el lambda para que se use la funcion solo cuando se presiona el boton porque cuando lo intente sin el lambda al abrir la ventana se ejecutaba la funcion
    boton_prestar = tk.Button(panel_formularios_prestamos, text="Prestar Libro Seleccionado", font="Verdana 12", foreground="#ffffff", background="#073650", borderwidth=0,
    command=lambda: prestar_libro(combobox_libro_prestar, entry_nombre_prestatario, tabla_prestamos))
    boton_prestar.pack(side="top", fill="x", pady=5)
    
    
    
    
    
    tk.Label(panel_formularios_prestamos, text="DEVOLVER LIBRO", font="Verdana 12 bold", fg="#960A0A", bg="#C7D3EE").pack(side="top", anchor="w", pady=(30, 5))

    tk.Label(panel_formularios_prestamos, text="Título a Devolver:", font="Verdana 10 bold", background="#C7D3EE").pack(side="top", anchor="w", pady=(10, 0))
    
    entry_titulo_devolver = tk.Entry(panel_formularios_prestamos, width=30)
    entry_titulo_devolver.pack(side="top", anchor="w", pady=(0, 10))

  #aqui igual como con el boton prestar
    boton_devolver = tk.Button(panel_formularios_prestamos, text="Devolver Libro", font="Verdana 12", foreground="#ffffff", background="#960A0A", borderwidth=0,
                              command=lambda: devolver_libro(entry_titulo_devolver, tabla_prestamos, combobox_libro_prestar)) 
    boton_devolver.pack(side="top", fill="x", pady=5)

    
   #esta es la unica funcion que esta aqui en main y es para actualizar la tabla de los libros prestados y el combobox para que solo aparezcan los que no se han prestado
    def inicializar_prestamos_ui():
        
        actualizar_listbox_prestamos(tabla_prestamos, obtener_prestados())
        
        actualizar_combobox_libros(combobox_libro_prestar, libros)

   #Para que se actualize cada 0.1 segundos como la hora y fecha
    ventana_prestamos.after(100, inicializar_prestamos_ui)

#Ventana libros
def crear_ventana_libros():

    root3 = tk.Toplevel(root)
    root3.title("Gestión de Libros")
    centrar_ventana(root3, 850, 700)

    
    #Igual tiene la misma estructura que todas las demas con la barra superior, el titulo, los entrys y las labels
    barra_superior_libros = tk.Frame(root3, background="#052B3F")
    barra_superior_libros.pack(fill="x")

    boton_salir = tk.Button(barra_superior_libros,text="Salir y Guardar",font="Verdana 10",foreground="#ffffff", background="#960A0A", borderwidth=0, command=lambda:(guardar_datos(),root3.destroy()))
    boton_salir.pack(padx=10, pady=10, side="right")

    etiqueta_titulo = tk.Label(barra_superior_libros, text="Gestión de Libros", font="Verdana 15 bold", foreground="#ffffff", background="#052B3F")
    etiqueta_titulo.pack(padx=10, pady=10, side="left")
    
    
    panel_principal_libros = tk.Frame(root3, background="#C7D3EE", padx=10, pady=10)
    panel_principal_libros.pack(expand=True, fill="both")
    
    
    panel_formularios = tk.Frame(panel_principal_libros, bg="#C7D3EE")
    panel_formularios.pack(side="left", fill="y", padx=10, pady=10)
    
    panel_lista = tk.Frame(panel_principal_libros, bg="#C7D3EE")
    panel_lista.pack(side="right", expand=True, fill="both", padx=10, pady=10)

    
    label_id_libro = tk.Label(panel_formularios, text="ID:", font="Verdana 10 bold", background="#C7D3EE")
    label_id_libro.pack(side="top", anchor="w", pady=(10, 0))
    entry_id_libro = tk.Entry(panel_formularios, width=30,) 
    entry_id_libro.pack(side="top", anchor="w", pady=(0, 5))

    
    label_titulo_libro = tk.Label(panel_formularios, text="Título:", font="Verdana 10 bold", background="#C7D3EE")
    label_titulo_libro.pack(side="top", anchor="w", pady=(5, 0))
    entry_titulo = tk.Entry(panel_formularios, width=30)
    entry_titulo.pack(side="top", anchor="w", pady=(0, 5))

    
    label_autor = tk.Label(panel_formularios, text="Autor:", font="Verdana 10 bold", background="#C7D3EE")
    label_autor.pack(side="top", anchor="w", pady=(5, 0))
    entry_autor = tk.Entry(panel_formularios, width=30)
    entry_autor.pack(side="top", anchor="w", pady=(0, 5))

    
    label_año = tk.Label(panel_formularios, text="Año:", font="Verdana 10 bold", background="#C7D3EE")
    label_año.pack(side="top", anchor="w", pady=(5, 0))
    entry_año = tk.Entry(panel_formularios, width=30) 
    entry_año.pack(side="top", anchor="w", pady=(0, 5))

    
    label_genero = tk.Label(panel_formularios, text="Género:", font="Verdana 10 bold", background="#C7D3EE")
    label_genero.pack(side="top", anchor="w", pady=(5, 0))
    entry_genero = tk.Entry(panel_formularios, width=30) 
    entry_genero.pack(side="top", anchor="w", pady=(0, 10))

    
    
    # crea la tabla para la ventana libros
    tabla_libros = ttk.Treeview(panel_lista, columns=("ID","Titulo","Autor","Año","Genero"), show="headings")

    # aqui son los encabezados y el nombre que cada uno tiene
    tabla_libros.heading("ID", text="ID")
    tabla_libros.heading("Titulo", text="Título")
    tabla_libros.heading("Autor", text="Autor")
    tabla_libros.heading("Año", text="Año")
    tabla_libros.heading("Genero", text="Género")

    # esto es para el tamaño de columnas
    tabla_libros.column("ID", width=80)
    tabla_libros.column("Titulo", width=180)
    tabla_libros.column("Autor", width=120)
    tabla_libros.column("Año", width=60)
    tabla_libros.column("Genero", width=90)

    tabla_libros.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)



    actualizar_listbox(tabla_libros, libros)

    #igual los botones con las funciones de los otros documentos
    boton_agregar_libro = tk.Button(panel_formularios, text="Agregar Libro", font="Verdana 12", foreground="#ffffff", background="#073650", borderwidth=0, 
                                     command=lambda: agregar_libro(entry_id_libro, entry_titulo, entry_autor, entry_año, entry_genero, tabla_libros))
    boton_agregar_libro.pack(side="top", fill="x", pady=5)
    
    
    boton_eliminar_libro = tk.Button(panel_formularios, text="Eliminar por Título", font="Verdana 12", foreground="#ffffff", background="#960A0A", borderwidth=0, 
                                     command=lambda: eliminar_libro(entry_titulo, tabla_libros))
    boton_eliminar_libro.pack(side="top", fill="x", pady=5)
    
    
    label_buscar_libro = tk.Label(panel_formularios, text="Buscar (Texto):", font="Verdana 10 bold", background="#C7D3EE")
    label_buscar_libro.pack(side="top", anchor="w", pady=20)

    entry_buscar_libro = tk.Entry(panel_formularios, width=30) 
    entry_buscar_libro.pack(side="top", anchor="w", padx=5)

    
    boton_buscar_libro = tk.Button(panel_formularios, text="Buscar", font="Verdana 12", foreground="#ffffff", background="#0C4F73", borderwidth=0,
                                   command=lambda: buscar_libro(entry_buscar_libro, tabla_libros))
    boton_buscar_libro.pack(side="top", fill="x", pady=5)

    
    boton_mostrar_todos = tk.Button(panel_formularios, text="Mostrar Todos", font="Verdana 12", foreground="#ffffff", background="#0C4F73", borderwidth=0,
                                   command=lambda: actualizar_listbox(tabla_libros, libros))
    boton_mostrar_todos.pack(side="top", fill="x", pady=5)


def crear_interfaz_usuario():
    # Ventana Usuarios
    root2 = tk.Toplevel(root)
    root2.title("Registro e Inicio de Sesión")
    centrar_ventana(root2,400,400)
    
    barra_superior = tk.Frame(root2,background="#052B3F")
    barra_superior.pack(fill="x")

    boton_salir = tk.Button(barra_superior, text="Salir", font="Verdana 10",foreground="#ffffff", background="#960A0A", borderwidth=0, command=root2.destroy)
    boton_salir.pack(padx=10, pady=10, side="right")


    etiqueta_titulo = tk.Label(barra_superior, text="Sistema de Acceso", font="Verdana 15 bold",foreground="#ffffff",background="#052B3F")
    etiqueta_titulo.pack(padx=10, pady=10, side="left")
    
    panel_principal_usuarios = tk.Frame(root2,background="#C7D3EE")
    panel_principal_usuarios.pack(expand=True, fill="both")


    label_id =tk.Label(panel_principal_usuarios, text="ID (Número):",font="Verdana 10 bold",background="#C7D3EE")
    label_id.pack(side="top", padx=0,pady=5)

    entry_id = tk.Entry(panel_principal_usuarios, width=15,)
    entry_id.pack(side="top", padx=0,pady=5)

    label_nombre= tk.Label(panel_principal_usuarios, text="Nombre:",font="Verdana 10 bold",background="#C7D3EE")
    label_nombre.pack(side="top", padx=0,pady=5)

    nombre_n_entry= tk.Entry(panel_principal_usuarios, width=15,)
    nombre_n_entry.pack(side="top", padx=0,pady=5)

    label_contraseña= tk.Label(panel_principal_usuarios, text="Contraseña:",font="Verdana 10 bold",background="#C7D3EE")
    label_contraseña.pack(side="top", padx=0,pady=5)

    entry_contraseña = tk.Entry(panel_principal_usuarios, show="*", width=15) 
    entry_contraseña.pack(side="top", padx=0,pady=5)


    # Botón para registrar usuario
    boton_registrar= tk.Button(panel_principal_usuarios, text="Registrar Usuario", width=18, command=lambda: registrar_usuario(nombre_n_entry,entry_id, entry_contraseña))
    boton_registrar.pack(side="left", padx=10)

    # Botón para iniciar sesión
    boton_iniciar_sesion= tk.Button(panel_principal_usuarios, text="Iniciar Sesión", width=18, command=lambda: iniciar_sesion(entry_id, entry_contraseña,etiqueta_usuario))
    boton_iniciar_sesion.pack(side="right", padx=10)

#creo el widget para graficas (echo por Laura)
def dibujar_grafica_en_frame(frame_contenedor, figura_mpl):
    #elimina cualquier widghet que haya
    for widget in frame_contenedor.winfo_children():
        widget.destroy()

    if figura_mpl is None:
        tk.Label(
            frame_contenedor, 
            text="No hay datos para mostrar el gráfico (Verifica los CSV).", 
            fg="red"
        ).pack(pady=20)
        return

    #creo las canvas
    canvas = FigureCanvasTkAgg(figura_mpl, master=frame_contenedor)
    canvas.draw() 
    canvas_widget = canvas.get_tk_widget()
    toolbar = NavigationToolbar2Tk(canvas, frame_contenedor)
    toolbar.update()
    
    #lo ordeno
    toolbar.pack(side=tk.BOTTOM, fill=tk.X)
    canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

#ahora la interfaz (echo por Laura)
def crear_interfaz_graficas():
    #crea una nueva ventana para mostrar y actualizar las gráficas de la biblioteca
    root_graficas = tk.Toplevel(root)
    root_graficas.title("Análisis de la Biblioteca - Gráficas")
    root_graficas.geometry("1200x600")
    barra_superior = tk.Frame(root_graficas, background="#052B3F")
    barra_superior.pack(fill="x")
    tk.Label(barra_superior, text="Gráficas de la Biblioteca", font="Verdana 15 bold", foreground="#ffffff", background="#052B3F").pack(padx=10, pady=10, side="left")
    
    #panel Principal y contenedores 
    panel_principal_graficas = tk.Frame(root_graficas, background="#C7D3EE")
    panel_principal_graficas.pack(expand=True, fill="both")
    frame_barras = tk.Frame(panel_principal_graficas, bd=2, relief=tk.GROOVE)
    frame_barras.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
    frame_pastel = tk.Frame(panel_principal_graficas, bd=2, relief=tk.GROOVE)
    frame_pastel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)

    #permite actualizar
    def actualizar_y_dibujar_graficas():
        #se lee el csv de nuevo
        figura_barras = graficas.generar_grafica_barras_generos_mpl()
        figura_pastel = graficas.generar_grafica_pastel_prestados_mpl()

        #se dibujan las graficas
        dibujar_grafica_en_frame(frame_barras, figura_barras)
        dibujar_grafica_en_frame(frame_pastel, figura_pastel)
        
    #aqui son los botones
    #salir
    tk.Button(barra_superior, text="Salir", font="Verdana 10", foreground="#ffffff", background="#960A0A", borderwidth=0, command=root_graficas.destroy).pack(padx=10, pady=10, side="right")
    
    #actualizar graficas
    boton_actualizar = tk.Button(barra_superior,text="Actualizar Gráficas", font="Verdana 10 bold", foreground="#ffffff", background="#960A0A", borderwidth=0, command=actualizar_y_dibujar_graficas)
    boton_actualizar.pack(padx=10, pady=10, side="right") 
    actualizar_y_dibujar_graficas()

#Ventana principal
root = tk.Tk()
root.title("Biblioteca")
centrar_ventana(root,800,600)


#con esta funcion importada se cargaran los datos de los documentos en csv
cargar_datos()

#Barra superior y sus widgets esta estructura se usa en todas las ventanas

barra_superior = tk.Frame(root,height=50,background="#052B3F")
barra_superior.pack(side="top",fill="x") 

boton_menu = tk.Button(barra_superior,text="≡",font="Verdana 15 bold",width=3,foreground="#ffffff", background="#052B3F", borderwidth=0,command=Mostrar_Ocultar_panel)
boton_menu.pack(padx=10,pady=10,side="left")

boton_salir = tk.Button(barra_superior,text="Salir y Guardar",font="Verdana 10",foreground="#ffffff", background="#960A0A", borderwidth=0, command=cerrar_aplicacion)
boton_salir.pack(padx=10,side="right")


etiqueta_biblioteca = tk.Label(barra_superior,text="Biblioteca",font="Verdana 20 bold",foreground="#ffffff",background="#052B3F")
etiqueta_biblioteca.pack(padx=10,pady=10,side="left")


etiqueta_hora = tk.Label(barra_superior, text="", font=("Verdana 10 bold"), foreground="#ffffff", background="#052B3F", justify="right")
etiqueta_hora.pack(padx=10, pady=5, side="right")

etiqueta_usuario = tk.Label(barra_superior, text="", font=("Verdana 10 bold"), foreground="#ffffff", background="#052B3F", justify="right")
etiqueta_usuario.pack(padx=10, pady=5, side="right")

#se crea el menú lateral y se ponen los botones
menu_lateral = tk.Frame(root,width=150,bg="#073650")
menu_lateral.pack(side=tk.LEFT,fill="y",expand=False)


boton_libros = tk.Button(menu_lateral,text="Libros",font="Verdana 15",foreground="#ffffff", background="#073650", borderwidth=0, command=crear_ventana_libros)
boton_libros.pack(fill="x", pady=10)

#para que al pasar el mouse el boton cambie de color
boton_libros.bind("<Enter>", pasar_mouse)
boton_libros.bind("<Leave>", quitar_mouse)


boton_prestamos = tk.Button(menu_lateral,text="Préstamos",font="Verdana 15",foreground="#ffffff", background="#073650", borderwidth=0, command=lambda: crear_interfaz_prestamos())
boton_prestamos.pack(fill="x", pady=10)


boton_prestamos.bind("<Enter>", pasar_mouse)
boton_prestamos.bind("<Leave>", quitar_mouse)


boton_usuarios = tk.Button(menu_lateral,text="Usuarios",font="Verdana 15",foreground="#ffffff", background="#073650", borderwidth=0, command=crear_interfaz_usuario)
boton_usuarios.pack(fill="x", pady=10)

boton_usuarios.bind("<Enter>", pasar_mouse)
boton_usuarios.bind("<Leave>", quitar_mouse)


boton_graficas = tk.Button(menu_lateral, text="Gráficas", font="Verdana 15", foreground="#ffffff", background="#073650", borderwidth=0, command=crear_interfaz_graficas)
boton_graficas.pack(fill="x", pady=10)

boton_graficas.bind("<Enter>", pasar_mouse)
boton_graficas.bind("<Leave>", quitar_mouse)

boton_informacion = tk.Button(menu_lateral,text="Más información",font="Verdana 10",foreground="#ffffff", background="#073650", borderwidth=0,command=mas_informacion)
boton_informacion.pack(side="bottom",fill="x", pady=10)

boton_informacion.bind("<Enter>", pasar_mouse)
boton_informacion.bind("<Leave>", quitar_mouse)


#El panel principal
panel_principal = tk.Frame(root,bg="#C7D3EE") 
panel_principal.pack(side=tk.RIGHT,fill="both",expand=True)

etiqueta_anuncio = tk.Label(panel_principal, text="     AVISO: Recuerda devolver los libros a tiempo. Horario de 7:00 a 20:00     ", font=("Verdana 13"), bg="#C7D3EE", fg="#960A0A")
etiqueta_anuncio.pack(side="bottom", fill="x", pady=10)

etiqueta_Nombres = tk.Label(panel_principal, text="""
                            
MANUAL DE USUARIO:
                            
¡Bienvenido a biblioteca!                         
Estamos felices de que uses nuestro sistema. 
Este manual te guiará rápidamente por las cuatro secciones principales para que puedas gestionar libros, usuarios y préstamos de forma sencilla.

(>) Usuarios
Esta es tu puerta de entrada al sistema. Aquí controlas quién accede a la aplicación.
Registrar Usuario: Ingresa un ID (Número), un Nombre, y una Contraseña. Presiona este botón para crear una nueva cuenta en el sistema.
Iniciar Sesión: Si ya tienes una cuenta, ingresa tu ID y Contraseña para acceder a todas las funciones. Si tienes éxito, el programa sabrá quién eres

(>) Libros
Esta es la sección de inventario, el corazón de la biblioteca. Desde aquí gestionas el catálogo y la base de datos de todos los títulos disponibles.
Agregar Nuevos Títulos: Para incluir un nuevo libro, llena todos los campos de la izquierda: ID, Título, Autor, Año y Género. Una vez completados, presiona el botón Agregar Libro.
Eliminar Títulos: Si un libro deseas eliminar un libro solo ingresa su titulo
Buscar y Filtrar: Utiliza los campos de texto para encontrar libros específicos o ver todo el catálogo
                            
(>) Prestamos
Seccion que te muestra los libros dispoibles, pide el tuyo solo con tu nombre
Devoluciones: Ingressa solo el titulo del libro a devolver. 

(>) Graficas
Esta sección te muestra un resumen visual de la actividad y el inventario de tu biblioteca, leyendo los datos de los archivos de libros y préstamos.                  
Gráfica de Barras: Muestra el Total de Libros por Género que tienes en inventario.
Gráfica de Pastel: Muestra la Distribución de Géneros más Prestados, basada en los registros de la sección Préstamos.
                                                                                   
""", font="Verdana 11 ",foreground="#000000",background="#C7D3EE", justify="left")
etiqueta_Nombres.pack(side="left", padx=20, pady=20)


#para que la hora este siempre actualizandose
actualizar_hora()
#para que la root principal nunca se cierre
root.mainloop()