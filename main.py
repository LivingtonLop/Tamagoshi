import os
import time

def clear_console():
    #En Windows es nt y en linux es posix
    os.system("cls" if os.name == "nt" else "clear")

def obtener_nombre_mascota():
    print("\nPor favor, introduce el nombre de tu mascota: ")
    nombre_mascota = input()
    return nombre_mascota

def obtener_dificultad():
    print("\nSelecciona la dificultad:")
    print("1. Fácil")
    print("2. Medio")
    print("3. Difícil")
    dificultad = input("\nElige la dificultad (1/2/3): ")
    return dificultad

def bienvenido():
    print("****************************")
    print("*                          *")
    print("*   Bienvenido al Juego    *")
    print("*         de               *")
    print("*       Tamagotchi!        *")
    print("*                          *")
    print("****************************")

    nombre_mascota = obtener_nombre_mascota()

    if nombre_mascota:
        clear_console()
        time.sleep(0.5)
        dificultad = obtener_dificultad()

        dificultadText = {
            "1":"Fácil",
            "2":"Medio",
            "3":"Dificil",
            "0":lambda : exit
        }

        if dificultad:
            clear_console()
            time.sleep(0.5)
            print("****************************")
            print("*                          *")
            print("*\nPet:", nombre_mascota," *")
            print("*                          *")
            print("*                          *")
            print("*\nDif:", dificultadText[dificultad]," *")
            print("****************************")

            time.sleep(5)
            return False

initialize = True

while initialize:
    clear_console()
    initialize = bienvenido()

