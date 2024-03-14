import time

from .animacion import Animacion

class Bienvenida (Animacion):
    def __init__(self):
        super().__init__()
 
    def obtener_nombre_mascota(self):
        print("\nPor favor, introduce el nombre de tu mascota: ")
        nombre_mascota = input()
        return nombre_mascota

    def obtener_dificultad(self):
        print("\nSelecciona la dificultad:")
        print("1. Fácil")
        print("2. Medio")
        print("3. Difícil")
        dificultad = input("\nElige la dificultad (1/2/3): ")
        return dificultad

    def bienvenido(self):
        
        print("****************************")
        print("*                          *")
        print("*   Bienvenido al Juego    *")
        print("*         de               *")
        print("*       Tamagotchi!        *")
        print("*                          *")
        print("****************************")

        nombre_mascota = self.obtener_nombre_mascota()

        if nombre_mascota:
            self.clear_console()
            time.sleep(0.5)
            dificultad = self.obtener_dificultad()

            dificultadText = {
                "1":"Fácil",
                "2":"Medio",
                "3":"Dificil"
            }

            if dificultad:
                self.clear_console()
                time.sleep(0.5)
                print("\nPet:", nombre_mascota," ")
                print("\nDif:", dificultadText[dificultad]," ")

                time.sleep(5)
                return False
