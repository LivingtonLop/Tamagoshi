import random
import json
import os

from .animacionNomal import AnimacionPet
from .managerKeys import ManagerKey
class Tamagoshi(AnimacionPet, ManagerKey):

    def __init__(self, petName, dificultadPet) -> None:
        super().__init__()
        self.name = petName
        self.dificultad = dificultadPet
        #default
        self.dormir = 0
        self.aburrimiento = 0
        self.hambre = 0
        self.limpieza = 0
        self.mov = True

    def live(self):
        self.clear_console()
        
        self.dormir += random.randint(0, 2)
        self.aburrimiento += random.randint(0, 3)
        self.hambre += random.randint(0, 4)
        self.limpieza += random.randint(0, 1)

        if self.dormir >= 10:
            print("¡Tu Tamagotchi está demasiado cansado! Necesita dormir.[d]")

        if self.aburrimiento >= 10:
            print("¡Tu Tamagotchi está muy aburrido! Dale algo para entretenerse.[e]")

        if self.hambre >= 10:
            print("¡Tu Tamagotchi está hambriento! Aliméntalo.[a]")
        
        if self.limpieza >= 10:
            print("¡Tu Tamagotchi está sucio! Debes limpiarlo.[l]")
                
        if self.key_push():
            tecla = self.get_key()
            accion = self.acciones.get(tecla)
            accion()
        else:
            self.animacionNormal(mov=self.mov)

        self.mov = not self.mov

    def dormirAnimacion(self):
        self.dormir = self.dormir - 10
        self.animacionDurmiendo()

    def limpiarAnimacion(self):
        self.limpieza = self.limpieza - 10
        self.animacionLimpiando()

    def alimentarAnimacion(self):
        self.hambre = self.hambre - 10
        self.animacionComiendo()

    def entretenerAnimacion(self):
        self.aburrimiento = self.aburrimiento - 10
        self.animacionJugando() 
        
    def savePet(self):
        pet = {"nombre": self.name, "dificultad": self.dificultad}
        folder = "../pets/pets.json"
        
        # Verificar si el archivo JSON existe
        if os.path.exists(folder):
            with open(folder, "r") as file_json:
                pets = json.load(file_json)
        else:
            pets = {}

        pets.update(pet)

        with open(folder, "w") as archivo_json:
            json.dump(pets, archivo_json, indent=4)
