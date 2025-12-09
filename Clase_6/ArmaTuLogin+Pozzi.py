
usuarios = {}



def guardar_usuario(dic_usuarios, nombre_usuario, password):
   
    dic_usuarios[nombre_usuario] = password
    print(f"✅ Usuario '{nombre_usuario}' registrado correctamente.\n")


def registrar_usuario(dic_usuarios):

    print("\n--- REGISTRO DE USUARIO ---")
    nombre = input("Ingresa un nombre de usuario nuevo: ")

   
    if nombre in dic_usuarios:
        print("⚠️ Ese nombre de usuario ya existe. Intenta con otro.\n")
        return

    password = input("Ingresa una contraseña: ")

    guardar_usuario(dic_usuarios, nombre, password)


def mostrar_usuarios(dic_usuarios):
   
    print("\n--- LISTA DE USUARIOS REGISTRADOS ---")
    if not dic_usuarios:
        print("No hay usuarios registrados todavía.\n")
        return

 
    for usuario, password in dic_usuarios.items():
        print(f"Usuario: {usuario} | Contraseña: {password}")
    print() 


def login(dic_usuarios):
   
    print("\n--- LOGIN DE USUARIO ---")
    nombre = input("Nombre de usuario: ")


    if nombre not in dic_usuarios:
        print("❌ Usuario no encontrado. Debes registrarte primero.\n")
        return

    password = input("Contraseña: ")


    if dic_usuarios[nombre] == password:
        print(f"✅ Login exitoso. ¡Bienvenido/a, {nombre}!\n")
    else:
        print("❌ Contraseña incorrecta.\n")




def menu():
  
    while True: 
        print("========== MENÚ ==========")
        print("1. Registrar usuario")
        print("2. Login")
        print("3. Mostrar usuarios registrados")
        print("4. Salir")
        print("==========================")

        opcion = input("Elige una opción (1-4): ")

        
        if opcion == "1":
            registrar_usuario(usuarios)
        elif opcion == "2":
            login(usuarios)
        elif opcion == "3":
            mostrar_usuarios(usuarios)
        elif opcion == "4":
            print("👋 Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción inválida, intenta nuevamente.\n")
            
if __name__ == "__main_":
    menu()