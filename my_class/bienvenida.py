import time
import os
import json

from .managerKeys import ManagerKey
class Bienvenida (ManagerKey):

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

    def bienvenido(self) -> list:
        Datos = self.saved_game()

        print(self.findScene(self.scene))  
        if type(Datos) is list:
            print(f"Mascotas Guardadas [c] : {Datos[0]}")
            print("Nueva Mascota [n]")
            print("Para salir presione [x]")

            while not self.key_push():
                tecla = self.get_key()
                accion = self.acciones_bienvenida.get(tecla)
                
                return accion()

        else:
            return self.nuevaPet
        

    def saved_game(self) -> list:

        file = "pets\\pets.json"
        pets = {}
        if os.path.exists(file):
            print("Partidas Guardadas")
            with open(file, "r") as file_json:
                pets = json.load(file_json)

        return list(pets.values()) if len(list(pets.values())) > 0 else False
    
    def nuevaPet(self) -> list:
        self.clear_console()
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
                
        return [nombre_mascota, dificultad]

    def continuarPet(self) -> list:
        return self.saved_game()