from usuarios import *

def mostrar_menu():

    print("----MENU----")
    print("1- Crear usuario")
    print("2- Mostrar usuarios")
    print("3- Buscar Usuarios(por ID)")
    print("4- Editar Usuario(por ID)")
    print("5- Eliminar usuarios(por ID)")
    print("6- Salir")


while True:

    mostrar_menu()

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":

        try:
            id = input("Ingrese una ID: ")

            if not id.isdigit():
                print("Error: la ID debe ser numerica")
                continue

            id = int(id)

        
            id_existente = False

            for usuario in usuarios:
                if usuario["id"] == id:
                    id_existente = True
                    break

            if id_existente:
                print("Error: ya existe un usuario con ese ID")
                continue

            nombre = input("Ingrese su nombre: ")

            if nombre.strip() == "" or not nombre.replace(" ", "").isalpha():
                print("Error: nombre invalido")
                continue

            
            email = input("Ingrese su email: ")

            if (
                email.strip() == ""
                or "@" not in email
                or "." not in email
                or " " in email
            ):
                print("Error: email invalido")
                continue

            edad = input("Ingrese su edad: ")

            if edad.strip() == "" or not edad.isdigit():
                print("Error: la edad debe ser un numero entero")
                continue

            edad = int(edad)

        
            if edad < 1 or edad > 115:
                print("Error: la edad debe estar entre 1 y 115 años")
                continue

            crear_usuario(id, nombre, email, edad)

        except ValueError:
            print("Error de datos")

    elif opcion == "2":

        mostrar_usuarios()

    elif opcion == "3":

        try:

            id = int(input("Ingrese el ID a buscar: "))

            buscar_usuario(id)

        except ValueError:

            print("Error: ingrese un ID valido")

    elif opcion == "4":

        try:

            id = int(input("Ingrese el ID del usuario a editar: "))

            editar_usuario(id)

        except ValueError:

            print("Error: ingrese un ID valido")

    elif opcion == "5":

        try:

            id = int(input("Ingrese el ID del usuario a eliminar: "))

            eliminar_usuario(id)

        except ValueError:

            print("Error: ingrese un ID valido")

    elif opcion == "6":

        print("Programa finalizado")
        break

    else:

        print("Opcion invalida")