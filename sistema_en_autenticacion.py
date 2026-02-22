usuarios = {}
def registrar_usuario():
    usuario = input("ingrese el nombre de usuario: ").strip()
    if usuario in usuarios:
        print("este usuario ya esta registrado.")
        return
    contrasena = input("ingrese la contraseña: ").strip()
    usuarios[usuario] = contrasena
    print(f"usuario '{usuario}' registrado correctamente.")
def validar_usuario():
    usuario = input("ingrese el nombre de usuario: ").strip()
    contrasena = input("ingrese la contraseña: ").strip()
    if usuario in usuarios and usuarios[usuario] == contrasena:
        print(f"bienvenido, {usuario}!")
    elif usuario in usuarios:
        print("contraseña incorrecta.")
    else:
        print("usuario no encontrado.")
def menu():
    while True:
        print("\n sistema de autenticacion ")
        print("1. registrar usuario")
        print("2. iniciar sesión")
        print("3. mostrar usuarios registrados")
        print("4. salir")
        opcion = input("seleccione una opcion: ")
        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            validar_usuario()
        elif opcion == "3":
            if usuarios:
                print("\n usuarios registrados:")
                for usuario in usuarios:
                    print(f"- {usuario}")
            else:
                print("no hay usuarios registrados.")
        elif opcion == "4":
            print("saliendo del sistema de autenticacion.")
            break
        else:
            print("opcion invalida, intente nuevamente.")
menu()