from pprint import pprint

libros = [
    # --- AMOR / ROMANCE ---
    {"titulo": "Bajo la Misma Estrella", "autor": "John Green", "año": 2012, "genero": "Amor"},
    {"titulo": "Orgullo y Prejuicio", "autor": "Jane Austen", "año": 1813, "genero": "Amor"},
    {"titulo": "Posdata: Te Amo", "autor": "Cecelia Ahern", "año": 2004, "genero": "Amor"},
    {"titulo": "A Tres Metros Sobre el Cielo", "autor": "Federico Moccia", "año": 1992, "genero": "Amor"},
    {"titulo": "Como Agua Para Chocolate", "autor": "Laura Esquivel", "año": 1989, "genero": "Amor"},
    {"titulo": "Yo Antes de Ti", "autor": "Jojo Moyes", "año": 2012, "genero": "Amor"},
    {"titulo": "Eleanor & Park", "autor": "Rainbow Rowell", "año": 2013, "genero": "Amor"},
    {"titulo": "After", "autor": "Anna Todd", "año": 2014, "genero": "Amor"},
    {"titulo": "Crepúsculo", "autor": "Stephenie Meyer", "año": 2005, "genero": "Amor"},
    {"titulo": "Bajo el Cielo Carmesí", "autor": "Mark Sullivan", "año": 2017, "genero": "Amor"},

    # --- TERROR ---
    {"titulo": "It", "autor": "Stephen King", "año": 1986, "genero": "Terror"},
    {"titulo": "El Resplandor", "autor": "Stephen King", "año": 1977, "genero": "Terror"},
    {"titulo": "Drácula", "autor": "Bram Stoker", "año": 1897, "genero": "Terror"},
    {"titulo": "Frankenstein", "autor": "Mary Shelley", "año": 1818, "genero": "Terror"},
    {"titulo": "Cementerio de Animales", "autor": "Stephen King", "año": 1983, "genero": "Terror"},
    {"titulo": "El Exorcista", "autor": "William Peter Blatty", "año": 1971, "genero": "Terror"},
    {"titulo": "El Color que Cayó del Cielo", "autor": "H. P. Lovecraft", "año": 1927, "genero": "Terror"},
    {"titulo": "La Llamada de Cthulhu", "autor": "H. P. Lovecraft", "año": 1928, "genero": "Terror"},
    {"titulo": "El Monje", "autor": "Matthew Lewis", "año": 1796, "genero": "Terror"},
    {"titulo": "Bird Box", "autor": "Josh Malerman", "año": 2014, "genero": "Terror"},

    # --- ACCIÓN / AVENTURA ---
    {"titulo": "Los Juegos del Hambre", "autor": "Suzanne Collins", "año": 2008, "genero": "Accion"},
    {"titulo": "El Código Da Vinci", "autor": "Dan Brown", "año": 2003, "genero": "Accion"},
    {"titulo": "El Señor de los Anillos", "autor": "J.R.R. Tolkien", "año": 1954, "genero": "Accion"},
    {"titulo": "Ready Player One", "autor": "Ernest Cline", "año": 2011, "genero": "Accion"},
    {"titulo": "Jurassic Park", "autor": "Michael Crichton", "año": 1990, "genero": "Accion"},
    {"titulo": "El Último Héroe del Olimpo", "autor": "Rick Riordan", "año": 2009, "genero": "Accion"},
    {"titulo": "La Isla del Tesoro", "autor": "Robert Louis Stevenson", "año": 1883, "genero": "Accion"},
    {"titulo": "Matar a un Reino", "autor": "Alexandra Christo", "año": 2018, "genero": "Accion"},
    {"titulo": "Alex Rider: Tormenta", "autor": "Anthony Horowitz", "año": 2000, "genero": "Accion"},
    {"titulo": "El Silmarillion", "autor": "J.R.R. Tolkien", "año": 1977, "genero": "Accion"}
]

#Funcion para agregar un libro 
def AggLibro():
    autor = input("Autor del libro: ")
    año = input("Año del libro: ")
    genero = input("Género del libro: ")

    return {"autor": autor,"año": año,"genero": genero}



#Función de consultar libros
def buscar_libro(consulta, libros):
    consulta = consulta.lower()
    resultados = []

    for libro in libros:
        if (consulta in libro["titulo"].lower() or
            consulta in libro["autor"].lower() or
            consulta in libro["genero"].lower()):
            resultados.append(libro)

    return resultados



def Menu(): #Menu 
    while True:
        print("\n----------Biblioteca ITSON----------")
        print("1. agregar libro")
        print("2. Eliminar ")
        print("3. Buscar libro")
        print("4. Libros")
        print("5. Salir")
        print("----------Biblioteca----------")

        #Agrega un libro 
        opcion = input("Digite la opcion del menu: ")
        print()
        if opcion == '1':
            titulo = input("Nombre del libro: ")

            nuevo_libro = AggLibro()  
            nuevo_libro["titulo"] = titulo  

            libros.append(nuevo_libro)  

            print("\nLibro agregado correctamente:")
            print(nuevo_libro)


        #Eliminar un libro
        elif opcion == '2':
            eliminar = input("Ingrese el título, autor o género del libro que desea eliminar: ").lower()
            encontrado = False
            for libro in libros:
                if (eliminar in libro["titulo"].lower()):
            
                    libros.remove(libro)
            
                    print("Libro eliminado correctamente")
                    break

            else:
                print("No se encontró ningún libro que coincida.")

    
        #Buscar libros por nombre, autor, genero y años
        elif opcion == '3':
            consulta = input("Buscar por título, autor o género: ")
            resultados = buscar_libro(consulta, libros)
            print()

            if resultados:
                for libro in resultados:
                    print(f"Título: {libro['titulo']}")
                    print(f"Autor:  {libro['autor']}")
                    print(f"Año:    {libro['año']}")
                    print(f"Género: {libro['genero']}")
                    print("-" * 30)
            else:
                print("No se encontraron resultados.")

        #Imprimir (Mostrar) Todos los libros
        elif opcion == '4':
            for libro in libros:
                print(f"Título: {libro['titulo']}")
                print(f"Autor:  {libro['autor']}")
                print(f"Año:    {libro['año']}")
                print("-" * 30)

        #Salir del programa
        elif opcion == '5':
            break

Menu()
