# cliente.py
import requests

def registrar():
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")
    datos = {"usuario": usuario, "contraseña": contraseña}
    respuesta = requests.post("http://localhost:5000/registro", json=datos)
    print(respuesta.json())

def login():
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")
    datos = {"usuario": usuario, "contraseña": contraseña}
    respuesta = requests.post("http://localhost:5000/login", json=datos)
    print(respuesta.json())

print("1. Registrar\n2. Login")
opcion = input("Elegí una opción: ")

if opcion == "1":
    registrar()
elif opcion == "2":
    login()
