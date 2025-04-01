import os
import subprocess


def ejecutar_Comando(comando : str):
    
    try:
        result = subprocess.run(
            comando,
            shell=True,
            check=True,
            text=True,
            capture_output=True
            )
        print(result.stdout.split())
    except subprocess.CalledProcessError as e:
        print(f"ERROR: {e.stdout.split()}")


def directorio_trabajo():
    path = input("\nIntroduce el directorio de trabajo completo: ")
    if os.path.isdir(path):
        os.chdir(path)
        print(f"El directorio de trabajo a cambiado a '{path}'")
    else:
        print("ERROR: El directorio establecido no existe.")

def crear_Repositorio():
    if os.path.isdir(".git"):
        print("Ya existe un repositorio en este directorio")
    else:
        ejecutar_Comando("git init")
        ejecutar_Comando("git branch -M main")
        print("Repositorio inicializado")

def crear_Rama():
    nombre_branch = input("Nombre de la nueva rama: ")
    ejecutar_Comando(f"git branch {nombre_branch}")

def cambiar_Rama():
    nombre_branch = input("Nombre de la rama a la que quieres cambiar: ")
    ejecutar_Comando(f"git checkout {nombre_branch}")

def mostrar_ficherosPendientes():
    ejecutar_Comando("git status")

def hacer_commit():
    msj_commit = input("Introduce un mensaje para el commit: ")
    ejecutar_Comando("git add .")
    ejecutar_Comando(f"git commit -m \"{msj_commit}\"")

def mostrar_historialCommits():
    ejecutar_Comando("git log --oneline")

def eliminar_rama():
    nombre_branch = input("Nombre de la rama que quieres eliminar: ")
    ejecutar_Comando(f"git branch -d {nombre_branch}")

def repositorio_remote():
    url_remote = input("URL del repositorio remoto: ")
    ejecutar_Comando(f"git remote add origin {url_remote}")
    ejecutar_Comando("git push -u origin main")

def hacer_pull():
    ejecutar_Comando("git pull")

def hacer_push():
    ejecutar_Comando("git push")
    

while True:

    print("\nDirectorio actual de trabajo")
    ejecutar_Comando("cd")


    print("\nSelecciona una opcion")
    print("1. Establecer el directorio de trabajo")
    print("2. Crear un nuevo repositorio")
    print("3. Crear una nueva rama")
    print("4. Cambiar de rama")
    print("5. Mostrar ficheros pendientes de hacer commit")
    print("6. Hacer commit (+add)")
    print("7. Mostrar el historial de commits")
    print("8. Eliminar rama")
    print("9. Establecer repositorio remoto")
    print("10. Hacer pull")
    print("11. Hacer push")
    print("12. Salir")

    respuesta = input("Selecciona una opcion: ")


    match respuesta:
        case "1":
            directorio_trabajo()
        case "2":
            crear_Repositorio()
        case "3":
            crear_Rama()
        case "4":
            cambiar_Rama()
        case "5":
            mostrar_ficherosPendientes()
        case "6":
            hacer_commit()
        case "7":
            mostrar_historialCommits()
        case "8":
            eliminar_rama()
        case "9":
            repositorio_remote()
        case "10":
            hacer_pull()
        case "11":
            hacer_push()
        case "12":
            print("\nEXIT: Saliendo del programa...")
            break
        case _:
            print("\nERROR: Opcion invalida, inserte un digito valido.")