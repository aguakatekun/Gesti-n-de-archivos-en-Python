import os
import base64
import shutil
def Menu():
    while True:
        print("Gestión de Ficheros con Python")
        print("Realizado por: Azan Umar")
        print()
        print("Menú de opciones")
        print()
        print("0.- Para salir.")
        print("1.- Crear un archivo.")
        print("2.- Eliminar un archivo.")
        print("3.- Leer de un archivo")
        print("4.- Renombrar un archivo.")
        print("5.- Encriptar el contenido de un archivo.")
        print("6.- Desencriptar el contenido de un archivo.")
        print("7.- Escribir en un fichero")
        print("8.- Copiar un fichero")
        opcion = input("Elija una acción a realizar: ")  # elige la opción del menú
        os.system('cls')
        if opcion == '0':
            break
        elif opcion == '1':
            crear_archivo()
        elif opcion == '2':
            eliminar_archivo()
        elif opcion == '3':
            leer()
        elif opcion == '4':
            renombrar()
        elif opcion == '5':
            encriptar()
        elif opcion == '6':
            desencriptar()
        elif opcion == '7':
            escribir_archivo()
        elif opcion == '8':
            copiar()
        else:
            print('Debes introducir un número válido')

# La "f" permite incluir expresiones dentro de una cadena
def crear_archivo():
    print("Qué desea crear?")
    ruta = input("Indica la ruta donde quieres crear el archivo: ")
    nombre = input("Indica el nombre del fichero: ")
    ruta_completa = os.path.join(ruta, nombre)
    
    if os.path.exists(ruta_completa):
        print("La ruta especificada ya existe, por lo que no se puede crear el archivo.")
        input("Pulse una tecla para continuar...")
    else:
        try:
            archivo = open(ruta_completa, "w")
            archivo.close()
            print(f"Fichero creado correctamente en {ruta_completa}")  
            input("Pulse una tecla para continuar...") 
        except FileNotFoundError:
             print("No se pudo encontrar la ruta del archivo")
             
#Solo se pueden eliminar archivos,no se puede eliminar directorios ya que con esta función se carece de permisos,se debería utilizar rmdir.
def eliminar_archivo():
    print("Qué desea eliminar?")
    ruta = input("Ingrese la ruta y el nombre del archivo a eliminar: ")
    if not os.path.exists(ruta):
         print("El archivo no existe.")
    else: 
        os.remove(ruta)
        print("El archivo se ha eliminado correctamente")

def leer():
    ruta = input("Ingrese la ruta y el nombre del archivo a leer: ")
    try:
        with open(ruta, 'r') as archivo:
            contenido = archivo.read()
            print("Contenido del archivo:",contenido)
    except FileNotFoundError:
        print("No se pudo encontrar la ruta del archivo")  

def renombrar():
    ruta = input("Ingrese la ruta y el nombre del archivo a renombrar: ")
    try:
        nueva_ruta = input("Ingrese la ruta del nombre nuevo del archivo: ")
        os.rename(ruta, nueva_ruta)
        print("Archivo renombrado correctamente.")
    except FileNotFoundError:
        print("No se pudo encontrar la ruta del archivo")

def encriptar():
    ruta = input("Introduzca la ruta del archivo que quiere encriptar: ")
    try:
        with open(ruta, 'rb') as archivo:
            contenido = archivo.read()
            contenido_encriptado = base64.b64encode(contenido)
        
        with open(ruta, 'wb') as archivo_encriptado:
            archivo_encriptado.write(contenido_encriptado)
        
        print("El contenido del archivo se ha encriptado correctamente.")
    except FileNotFoundError:
        print("No se pudo encontrar la ruta del archivo")

def desencriptar():
    ruta = input("Introduzca la ruta del archivo que quiere desencriptar: ")
    try:
        with open(ruta, 'rb') as archivo:
            contenido_encriptado = archivo.read()
            contenido_desencriptado = base64.b64decode(contenido_encriptado)
        
        with open(ruta, 'wb') as archivo_desencriptado:
            archivo_desencriptado.write(contenido_desencriptado)
        
        print("El contenido del archivo se ha desencriptado correctamente.")
    except FileNotFoundError:
        print("No se pudo encontrar la ruta del archivo")

def escribir_archivo():
    ruta = input("Ingrese la ruta y el nombre del archivo en el cual quiere escribir: ")
    if not os.path.exists(ruta):
        print("El archivo no existe.")
    else: 
        texto = input("Qué desea escribir? ")
        with open(ruta,'a') as archivo:
            archivo.write('\n'+texto)
        print("El texto se ha escrito correctamente: ",texto)
        input("Pulse una tecla para continuar...")

def copiar():
  
    origen = input("Ingrese la ruta del archivo origen: ")
    destino = input("Ingrese la ruta del archivo destino: ")

    if not os.path.exists(origen):
        print("La ruta ORIGEN no existe:",origen)
        input("Pulsa una tecla para continuar...")
    if not os.path.exists(destino):
        print("La ruta DESTINO no existe:",origen)
        input("Pulsa una tecla para continuar...")
    try:
        shutil.copy(origen, destino)
        print("La copia se ha realizado correctamente VAMOOOOSS")
    except Exception as e:
        print(f"Error al copiar el archivo: {e}")
    input("Pulsa una tecla para continuar...")
Menu()
