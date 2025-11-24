usuarios={} #Se guardan los ID y contraseñas

def registrar_usuario():
    print("\n*** Registro de nuevo usuario ***")

    ID_nuevo= int(input("Escriba un ID nuevo(solo números): "))

    if ID_nuevo in usuarios: #Verificacion que sea un ID nuevo
        print("Este ID ya esta registrado, intente con otro") 
        return
    
    contraseña_nueva= input("Escriba su contraseña: ")
    usuarios[ID_nuevo]= contraseña_nueva
    print("El usuario se ha registrado con exito ")

def iniciar_sesion():
    usuario=int(input("Ingrese su ID(recuerde, solo números): "))

    if usuario not in usuarios: #Verificacion que el usuario este registrado
        print("El usuario no esta registrado, intentelo de nuevo")
        return
    
    contraseña= input(("Ingrese su contraseña: "))

    if usuarios[usuario]!=contraseña: #Verificar si la contraseña esta registrada
        print("Contraseña incorrecta")
        return
    else:
        print("Se inicio correctamente de sesión, bienvenido usuario!!")


