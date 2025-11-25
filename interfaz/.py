from pprint import pprint


libros = []


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

#Consultar libros
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
        print("1. Agregar ")
        print("2. agregar libro")
        print("3. Eliminar ")
        print("4. Salir")
        print("5. Libros")
        print("6. Buscar libro")
        print("----------Biblioteca----------")

        


        elif opcion == '3':
            input("Que libro desea eliminar")

        elif opcion == '5':
            for libro in libros:
                print(f"Título: {libro['titulo']}")
                print(f"Autor:  {libro['autor']}")
                print(f"Año:    {libro['año']}")
                print("-" * 30)
        #Buscar libros por nombre, autor, genero y años
        elif opcion == '6':
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

        elif opcion == '4':
            break
   


Menu()
