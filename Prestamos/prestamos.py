# ---------------------------------------------
# Sistema de Préstamos de Biblioteca
# Funciones: Registrar préstamo, Consultar, Devoluciones
# ---------------------------------------------

prestamos = {}   # Diccionario: clave = ID Préstamo, valor = info del préstamo
contador_id = 1  # Genera IDs automáticos


def registrar_prestamo():
    global contador_id

    print("\n--- Registrar Préstamo ---")
    usuario = input("Nombre del usuario: ")
    libro = input("Título del libro: ")
    fecha = input("Fecha del préstamo (dd/mm/aaaa): ")

    prestamos[contador_id] = {
        "usuario": usuario,
        "libro": libro,
        "fecha": fecha,
        "devuelto": False
    }

    print(f"\nPréstamo registrado correctamente con ID: {contador_id}\n")
    contador_id += 1


def consultar_prestamos():
    print("\n--- Préstamos Activos ---")

    hay_activos = False
    for id_prestamo, datos in prestamos.items():
        if not datos["devuelto"]:
            hay_activos = True
            print(f"""
ID: {id_prestamo}
Usuario: {datos['usuario']}
Libro: {datos['libro']}
Fecha: {datos['fecha']}
Estado: {"No devuelto"}
-----------------------------
""")
    if not hay_activos:
        print("No hay préstamos activos.\n")


def devolver_libro():
    print("\n--- Registrar Devolución ---")
    try:
        id_prestamo = int(input("Ingresa el ID del préstamo: "))

        if id_prestamo in prestamos and not prestamos[id_prestamo]["devuelto"]:
            prestamos[id_prestamo]["devuelto"] = True
            print(f"\nLibro '{prestamos[id_prestamo]['libro']}' devuelto correctamente.\n")
        else:
            print("\nID no encontrado o ya devuelto.\n")

    except ValueError:
        print("\nError: Debes ingresar un número.\n")


def menu():
    while True:
        print("""
=========== BIBLIOTECA ===========
1. Registrar préstamo
2. Consultar préstamos activos
3. Registrar devolución
4. Salir
==================================
""")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            registrar_prestamo()
        elif opcion == "2":
            consultar_prestamos()
        elif opcion == "3":
            devolver_libro()
        elif opcion == "4":
            print("\nSaliendo del sistema...")
            break
        else:
            print("\nOpción no válida. Intenta de nuevo.\n")


# Ejecutar menú principal
menu()
