from tkinter import *
from tkinter import filedialog as f
from tkinter import messagebox, simpledialog
from io import open
import os
from cryptography.fernet import Fernet

# Comprobar si existe un archivo de clave, si no, generar una nueva clave y guardarla
key_file = "key.key"
if not os.path.exists(key_file):
    key = Fernet.generate_key()
    with open(key_file, "wb") as key_file:
        key_file.write(key)

# Cargar la clave desde el archivo
with open(key_file, "rb") as key_file:
    key = key_file.read()

cipher_suite = Fernet(key)

title = "Bloc de notas"

root = Tk()
root.title(title)

# URL del archivo
url_file = ""
password_file = "password.pkl"

# Funciones
def new_file():
    global url_file
    text.delete(1.0, "end")
    url_file = ""
    root.title(url_file + title)

def open_file():
    global url_file
    url_file = f.askopenfilename(initialdir=".",filetype=(("Archivos de texto", "*.txt"),),title="Abrir archivo")
    if url_file != "":
        password = simpledialog.askstring("Input", "Ingrese la contraseña", show='*')
        if password and verify_password(password):
            with open(url_file, "rb") as file:
                encrypted_content = file.read()
            decrypted_content = cipher_suite.decrypt(encrypted_content)
            content = decrypted_content.decode('utf-8')
            text.delete(1.0, "end")
            text.insert('insert', content)
            root.title(url_file + title)
        else:
            messagebox.showerror("Error", "Contraseña incorrecta o no ingresada.")

def save_file():
    global url_file
    password = simpledialog.askstring("Input", "Ingrese la contraseña para encriptar el archivo", show='*')
    if password:
        save_password(password)
        if url_file:
            content = text.get(1.0, "end-1c")
            encrypted_content = cipher_suite.encrypt(content.encode('utf-8'))
            with open(url_file, 'wb') as file:
                file.write(encrypted_content)
            root.title("Archivo guardado " + url_file + title)
        else:
            file = f.asksaveasfile(title="Save file", mode='w', defaultextension=".txt")
            if file is not None:
                url_file = file.name
                content = text.get(1.0, "end-1c")
                encrypted_content = cipher_suite.encrypt(content.encode('utf-8'))
                with open(url_file, 'wb') as file:
                    file.write(encrypted_content)
                root.title("Archivo guardado " + url_file + title)
            else:
                url_file = ""
                root.title("Guardado cancelado " + url_file + title)
    else:
        messagebox.showerror("Error", "Contraseña incorrecta o no ingresada.")

def save_password(password):
    encrypted_password = cipher_suite.encrypt(password.encode('utf-8'))
    with open(password_file, "wb") as file:
        file.write(encrypted_password)

def load_password():
    if os.path.exists(password_file):
        with open(password_file, "rb") as file:
            encrypted_password = file.read()
        decrypted_password = cipher_suite.decrypt(encrypted_password)
        return decrypted_password.decode('utf-8')
    else:
        return None

def verify_password(password):
    saved_password = load_password()
    if saved_password is not None and saved_password == password:
        return True
    else:
        return False
    
def change_theme_dark():
    text.config(bg="#2b2b2b", fg="white", insertbackground="white")

def change_theme_light():
    text.config(bg="white", fg="black", insertbackground="black")


# Menú
bar = Menu(root)

file_menu = Menu(bar, tearoff=0)
file_menu.add_command(label="Nuevo archivo", command=new_file)
file_menu.add_separator()
file_menu.add_command(label="Abrir archivo", command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Guardar archivo", command=save_file)
file_menu.add_separator()
bar.add_cascade(menu=file_menu, label="Archivo")

theme_menu = Menu(bar, tearoff=0)
theme_menu.add_command(label="Dark", command=change_theme_dark)
theme_menu.add_command(label="Light", command=change_theme_light)
bar.add_cascade(menu=theme_menu, label="Theme")

file_menu.add_separator()
file_menu.add_command(label="Salir", command=root.quit)

# Caja de texto
text = Text(root)
text.pack(fill="both", expand=1)
text.config(bd=0, padx=6, pady=5, font=("Arial", 12))

# Ejecutar
root.config(menu=bar)
root.mainloop()
