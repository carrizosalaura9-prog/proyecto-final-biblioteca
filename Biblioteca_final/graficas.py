#codigo echo por Laura (^.^)
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import os
import tkinter as tk 

#paso los nombres de los csv
RUTA_LIBROS = 'libros.csv'
RUTA_PRESTAMOS = 'prestamos.csv'


#funcion para cargar los datos
def cargar_csv(ruta):
    if not os.path.exists(ruta):
        print(f"Error: El archivo '{ruta}' no se encontró.")
        return pd.DataFrame()
    try:
        df = pd.read_csv(ruta)
        df.columns = df.columns.str.lower().str.strip()
        return df
    except Exception as e:
        print(f"Error al leer el archivo '{ruta}': {e}")
        return pd.DataFrame()


#aqui es la grafica de barras
def generar_grafica_barras_generos_mpl():
    plt.close('all') 

    df_libros = cargar_csv(RUTA_LIBROS)

    if df_libros.empty or 'genero' not in df_libros.columns:
        print("Error en datos de libros.csv para barras.")
        return None

    conteo_generos = df_libros['genero'].value_counts()
    if conteo_generos.empty:
        print("No hay datos de géneros para la gráfica de barras.")
        return None

    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111) 

    conteo_generos.plot(kind='bar', color='darkgreen', ax=ax)
    #formato
    ax.set_title('Cantidad Total de Libros por Género', fontsize=12)
    ax.set_xlabel('Género', fontsize=10)
    ax.set_ylabel('Número de Libros', fontsize=10)
    ax.tick_params(axis='x', rotation=45)
    ax.grid(axis='y', linestyle='--')
    
    for i, v in enumerate(conteo_generos):
        ax.text(i, v + 0.1, str(v), color='black', ha='center', fontweight='bold', fontsize=8)
    
    fig.tight_layout()
    return fig



#grafica de pastel
def generar_grafica_pastel_prestados_mpl():
    plt.close('all') 
    
    df_libros = cargar_csv(RUTA_LIBROS)
    df_prestamos = cargar_csv(RUTA_PRESTAMOS)

    if df_libros.empty or df_prestamos.empty:
        print("Error al cargar libros.csv o prestamos.csv para pastel.")
        return None

    COLUMNA_UNION = 'titulo'
    COLUMNA_GENERO = 'genero'

    if COLUMNA_UNION not in df_libros.columns or COLUMNA_UNION not in df_prestamos.columns:
         print(f"Error: La columna de unión ('{COLUMNA_UNION}') no se encontró en ambos archivos.")
         return None
    
    df_prestamos_con_genero = pd.merge(
        df_prestamos, 
        df_libros[[COLUMNA_UNION, COLUMNA_GENERO]], 
        on=COLUMNA_UNION, 
        how='left'
    )
    
    #inicio conteo para registrar prestamos
    conteo_prestamos_por_genero = df_prestamos_con_genero[COLUMNA_GENERO].value_counts()
    
    if conteo_prestamos_por_genero.empty or conteo_prestamos_por_genero.sum() == 0:
        print("No hay datos de géneros válidos en los préstamos después de la unión.")
        return None

    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111) 
    
    conteo_prestamos_por_genero.plot(
        kind='pie', 
        autopct='%1.1f%%', 
        startangle=90, 
        wedgeprops={'edgecolor': 'black'},
        textprops={'fontsize': 8},
        ax=ax 
    )
    
    ax.set_title('Distribución de Géneros más Prestados', fontsize=12)
    ax.set_ylabel('') 
    
    fig.tight_layout()
    return fig