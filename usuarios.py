import json

ARCHIVO = "usuarios.json"

usuarios = []


def cargar_usuarios():

    global usuarios

    try:
        with open(ARCHIVO, "r") as archivo:
            usuarios = json.load(archivo)

    except FileNotFoundError:
        usuarios = []


def guardar_usuarios():

    with open(ARCHIVO, "w") as archivo:
        json.dump(usuarios, archivo, indent=4)


cargar_usuarios()


def crear_usuario(id, nombre, email, edad):

    if edad < 1 or edad > 115:
        print("Error: la edad debe estar entre 1 y 115 años")
        return

    usuario = {
        "id": id,
        "nombre": nombre,
        "email": email,
        "edad": edad
    }

    usuarios.append(usuario)

    guardar_usuarios()

    print("Usuario creado correctamente")


def mostrar_usuarios():

    if len(usuarios) == 0:
        print("No hay usuarios cargados")

    else:
        for usuario in usuarios:

            print("----------------")
            print(f"ID: {usuario['id']}")
            print(f"Nombre: {usuario['nombre']}")
            print(f"Email: {usuario['email']}")
            print(f"Edad: {usuario['edad']}")


def buscar_usuario(id):

    for usuario in usuarios:

        if usuario["id"] == id:

            print("Usuario encontrado")
            print(usuario)
            return

    print("Usuario no encontrado")


def editar_usuario(id):

    for usuario in usuarios:

        if usuario["id"] == id:

            nuevo_nombre = input("Nuevo nombre: ")
            nuevo_email = input("Nuevo email: ")
            nueva_edad = int(input("Nueva edad: "))

            if nueva_edad < 1 or nueva_edad > 115:
                print("Error: la edad debe estar entre 1 y 115 años")
                return

            usuario["nombre"] = nuevo_nombre
            usuario["email"] = nuevo_email
            usuario["edad"] = nueva_edad

            guardar_usuarios()

            print("Usuario editado correctamente")
            return

    print("Usuario no encontrado")


def eliminar_usuario(id):

    for usuario in usuarios:

        if usuario["id"] == id:

            usuarios.remove(usuario)

            guardar_usuarios()

            print("Usuario eliminado correctamente")
            return

    print("Usuario no encontrado")