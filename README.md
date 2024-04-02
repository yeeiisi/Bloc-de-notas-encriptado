# Bloc-de-notas-encriptado

Este es un simple bloc de notas en Python utilizando la biblioteca Tkinter. El bloc de notas tiene la capacidad de encriptar las notas al guardarlas utilizando una contraseña proporcionada por el usuario.

## Funcionalidades

- Encripta las notas al guardarlas mediante una contraseña.
- Utiliza la biblioteca `cryptography.fernet` y Fernet para el cifrado.
- Genera una clave de cifrado que se guarda en un archivo `key.key`, cifrando también la contraseña.
- Guarda una contraseña encriptada en el archivo `password.pkl` para bloquear el proceso de cifrado y descifrado.
- Permite abrir, guardar, crear un nuevo archivo y salir a través de un menú desplegable.
- Implementa la biblioteca `os`, `filedialog`, `io`, `messagebox` y `simpledialog` para interactuar con los archivos y el usuario.
- Incluye un menú para cambiar el tema de la ventana del bloc entre oscuro y claro.

## Uso

1. Ejecuta el script Python `bloc.py`.
2. Utiliza las opciones del menú desplegable para abrir, guardar, crear un nuevo archivo o salir.
3. Se te solicitará una contraseña al guardar una nota, esta contraseña se utilizará para encriptar la nota.
4. También se te pedirá la misma contraseña al abrir un archivo encriptado para desbloquear el contenido.
5. Para su demostración; se proporciona un archivo `prueba1.txt`, el cual contiene un mensaje cifrado. Para descifrarlo, usar la contraseña: `12345`.

## Imágenes del programa
![Captura de pantalla 2024-04-02 162440](https://github.com/yeeiisi/Bloc-de-notas-encriptado/assets/127243820/91b6479a-486b-4525-b520-51c00257fd88)
![Captura de pantalla 2024-04-02 162615](https://github.com/yeeiisi/Bloc-de-notas-encriptado/assets/127243820/20b10b93-9102-415f-ad2b-8d65f90fde7f)
![Captura de pantalla 2024-04-02 162624](https://github.com/yeeiisi/Bloc-de-notas-encriptado/assets/127243820/e04dac94-47c0-4469-b0ee-15c59a712ebb)
![Captura de pantalla 2024-04-02 162639](https://github.com/yeeiisi/Bloc-de-notas-encriptado/assets/127243820/97e1c1da-b6b5-4012-bdf6-c9a3e8547c20)
![Captura de pantalla 2024-04-02 162706](https://github.com/yeeiisi/Bloc-de-notas-encriptado/assets/127243820/51270132-d8b8-4b4d-a37b-314ca3151b2f)



## Adicional
- Ejecuta el archivo `descifrar.py`, para descifrar el contenido de la nota, sin necesidad de abrir el `bloc.py`.
- Toma la clave de cifrado del archivo key.key para facilitar el proceso y solicitará la contraseña ingresada al guardar el archivo.

## Requisitos

Para ejecutar el Bloc de Notas Encriptado, asegúrate de tener instalado Python 3.x y las siguientes bibliotecas:

- `cryptography`
- `tkinter`

# Windows
Puedes instalar estas bibliotecas utilizando `pip`, el administrador de paquetes de Python. Abre una terminal (tecla windows + r, escribir "cmd" y pulsar INTRO) o línea de comandos y ejecuta los siguientes comandos:
(generalmente tkinter viene instalado con python)

pip install cryptography
pip install tkinter
pip install nombre_de_biblioteca

# Si estás en un entorno Linux y no tienes tkinter instalado, ejecuta este comando en una terminal:
sudo apt-get install python3-tk

## Notas

- `NO USAR COMO MÉTODO DE ENCRIPTACIÓN DE INFORMACIÓN IMPORTANTE O FRÁGIL` ya que tanto la contraseña introducida, como el mensaje se pueden descifrar con la contraseña generada
  por Fernet, que está guardada en el archivo key.key.
- `ESTO ES UN EJEMPLO DE ENCRIPTACIÓN, LA BRECHA DE SEGURIDAD SE DEBE MEJORAR`.

## Contribuciones

Las contribuciones son bienvenidas. Siéntete libre de abrir un problema o enviar una solicitud de extracción para mejorar este proyecto.

