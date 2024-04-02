from cryptography.fernet import Fernet, InvalidToken
import os
from tkinter import simpledialog

# Nombre del archivo que contiene el mensaje cifrado
file_name = "prueba1.txt"

# Comprobar si existe un archivo de clave
key_file = "key.key"
if not os.path.exists(key_file):
    print("No se encontró el archivo de clave.")
    exit()

# Leer la clave del archivo
with open(key_file, 'rb') as file:
    key = file.read()

# Leer el mensaje cifrado desde el archivo
with open(file_name, "rb") as file:
    encrypted_message = file.read()

# Pedir contraseña al usuario
password = simpledialog.askstring("Input", "Ingrese la contraseña para descifrar el archivo", show='*')
if not password:
    print("Contraseña no ingresada.")
    exit()

# Verificar contraseña y descifrar el mensaje
try:
    cipher_suite = Fernet(key)
    decrypted_message = cipher_suite.decrypt(encrypted_message)
    print("Mensaje descifrado:")
    print(decrypted_message.decode('utf-8'))
except InvalidToken:
    print("Contraseña incorrecta.")
