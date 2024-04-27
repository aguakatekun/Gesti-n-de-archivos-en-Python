import os

def Menu():
    while True:
        print("0.- Para salir.")
        print("1.- Crear un directorio / archivo.")
        print("2.- Eliminar un directorio o archivo.")
        print("3.- Mover un directorio o archivo.")
        print("4.- Renombrar un directorio o archivo.")
        print("5.- Encriptar el contenido de un archivo.")
        print("6.- Decodificar el contenido de un archivo.")
        print("7.- Escribir el contenido de un archivo")
        opcion = int(input("Elija una acción a realizar: ")) # elige la opción del menú
        
        if opcion == 0:
            break
        elif opcion == 1:
            crear_archivo()
        elif opcion == 2:
            print("2")
        elif opcion == 3:
            print("3")
        elif opcion == 4:
            print("4")
        elif opcion == 5:
            print("5")
        elif opcion == 6:
            print("6")
        elif opcion == 7:
            print("7")
        else:
            print('Debes introducir un número válido')

def crear_archivo():
    print("Que desea crear?")
    print("A.Archivo")
    print("B.Directorio")
    opcion = input("Elija una acción a realizar: ") 
    if opcion == 'A':
        ruta = input("Ingrese la ruta y el nombre del archivo a crear: ")
        if os.path.exists(ruta): # comprobar si la ruta existe
            print("La ruta especificada ya existe por lo que no se puede crear el archivo.")
        else:
            archivo = open(ruta, "w") # Abriendo y creando archivo
            archivo.close() # Cerrar el archivo
            print("El archivo se ha creado correctamente")

    else:
            if os.path.exists(ruta): # comprobar si la ruta existe
                print("La ruta especificada ya existe por lo que no se puede crear el archivo.")
            else:
                ruta = input("Ingrese la ruta y el nombre del directorio a crear: ")
                os.mkdir(ruta) 
                print("El directorio se ha creado correctamente")
Menu()
