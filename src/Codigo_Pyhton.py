import os
import json

# Diccionario hash para asociar nombre con archivo
clientes = {}

# Cargar clientes ya existentes (si hay)
def cargar_clientes():
    if os.path.exists("Clientes.json"):
        with open("clientes.json", "r") as file:
            global clientes
            clientes = json.load(file)

def guardar_clientes():
    with open("clientes.json", "w") as file:
        json.dump(clientes, file)

# Crear cliente nuevo
def crear_clientes(nombre, descripcion):
    if nombre in clientes:
        print(f"⚠️ El cliente '{nombre}' ya existe.")
        return
    archivo = f"{nombre}.txt"
    with open(archivo, "w") as file:
        file.write(f"Servicio solicitado: {descripcion}\n")
    clientes[nombre] = archivo
    guardar_clientes()
    print(f"✅ Cliente '{nombre}' creado y registrado.")

# Consultar cliente
def consultar_clientes(nombre):
    if nombre not in clientes:
        print(f"❌ Cliente '{nombre}' no encontrado.")
        return
    with open(clientes[nombre], "r") as file:
        print(f"📂 Informacion del cliente '{nombre}':\n")
        print(file.read())

# Actualizar cliente
def actualizar_clientes(nombre, nueva_descripcion):
    if nombre not in clientes:
        print(f"❌ Cliente '{nombre}' no encontrado.")
        return
    with open(clientes[nombre], "a") as file:
        file.write(f"Nuevo servicio solicitado: {nueva_descripcion}\n")
    print(f"🔁 Cliente '{nombre}' actualizado.")

# Eliminar cliente
def eliminar_cliente(nombre):
    if nombre not in clientes:
        print(f"❌ Cliente '{nombre}' no encontrado.")
        return
    os.remove(clientes[nombre])
    del clientes[nombre]
    guardar_clientes()
    print (f"🗑️ Cliente '{nombre}' eliminado.")
    
# Mostrar lista de clientes
def listar_clientes():
    if not clientes:
        print("📭 No hay clientes registrados.")
    else:
        print("📋 Lista de clientes:")
        for nombre in clientes:
            print(f" - {nombre}")

# Menu principal
def menu():
    cargar_clientes()
    while True:
        print("\n📦 Gestion de Clientes")
        print("1. Crear cliente")
        print("2. Consultar cliente")
        print("3. Actualizar cliente")
        print("4. Eliminar cliente")
        print("5. Listar todos los clientes")
        print("6. Salir")
        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            nombre = input("Nombre del cliente: ")
            desc = input("Descripción del servicio: ")
            crear_clientes(nombre, desc)
        elif opcion == "2":
            nombre = input("Nombre del cliente: ")
            consultar_clientes(nombre)
        elif opcion == "3":
            nombre = input("Nombre del cliente: ")
            nueva_desc = input("Nueva descripción del servicio: ")
            actualizar_clientes(nombre, nueva_desc)
        elif opcion == "4":
            nombre = input("Nombre del cliente: ")
            eliminar_cliente(nombre)
        elif opcion == "5":
            listar_clientes()
        elif opcion == "6":
            print("👋 ¡Hasta luego!")
            break
        else:
            print("❌ Opción inválida")

menu()
