import requests

BASE_URL = "http://localhost:5000"

def registrar():
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")
    datos = {"usuario": usuario, "contraseña": contraseña}
    respuesta = requests.post(f"{BASE_URL}/registro", json=datos)
    print(respuesta.json())

def login():
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")
    datos = {"usuario": usuario, "contraseña": contraseña}
    respuesta = requests.post(f"{BASE_URL}/login", json=datos)
    print(respuesta.json())

def crear_tarea():
    usuario = input("Usuario: ")
    descripcion = input("Descripción de la tarea: ")
    datos = {"usuario": usuario, "descripcion": descripcion}
    respuesta = requests.post(f"{BASE_URL}/tareas", json=datos)
    print(respuesta.json())

def ver_tareas():
    usuario = input("Usuario: ")
    respuesta = requests.get(f"{BASE_URL}/tareas", params={"usuario": usuario})
    if respuesta.status_code == 200:
        tareas = respuesta.json()
        if tareas:
            print("\n📋 Tareas del usuario:")
            for tarea in tareas:
                print(f"[{tarea['id']}] {tarea['descripcion']} - Estado: {tarea['estado']}")
        else:
            print("🚫 No hay tareas registradas.")
    else:
        print(respuesta.json())
        
if __name__ == "__main__":
    print("📌 Menú:")
print("1. Registrar usuario")
print("2. Iniciar sesión")
print("3. Crear tarea")
print("4. Ver tareas")
opcion = input("Elegí una opción (1/2/3/4): ")

if opcion == "1":
    registrar()
elif opcion == "2":
    login()
elif opcion == "3":
    crear_tarea()
elif opcion == "4":
    ver_tareas()
else:
    print("Opción no válida")