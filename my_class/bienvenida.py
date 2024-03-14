import time

from .animacion import Animacion

class Bienvenida (Animacion):

    scene = "animations_ascii/bienvenida"
    scene2 = "animations_ascii/dificultad"
    resume = "animations_ascii/resumen"
    
    def __init__(self):
        super().__init__()
 
    def obtener_nombre_mascota(self):
        print("\nPor favor, introduce el nombre de tu mascota: ")
        nombre_mascota = input()
        return nombre_mascota

    def obtener_dificultad(self):
        print(self.findScene(self.scene2))        

        dificultad = input("\nElige la dificultad (1/2/3): ")
        return dificultad

    def bienvenido(self):

        print(self.findScene(self.scene))        

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
                
                print(self.findScene(self.resume).format(nombre_mascota = nombre_mascota,dificultad_text =dificultadText[dificultad]))

                time.sleep(5)
                return False
