import random
import json
import os

from .animacionNomal import AnimacionPet
from .managerKeys import ManagerKey
class Tamagoshi(ManagerKey):

    def __init__(self, petName, dificultadPet,domir = 0, aburrimiento = 0, hambre = 0, limpieza = 0) -> None:
        super().__init__()
        self.name = petName
        self.dificultad = dificultadPet
        #default
        self.dormir = domir
        self.aburrimiento = aburrimiento
        self.hambre = hambre
        self.limpieza = limpieza
        self.mov = True

    def live(self):
        self.clear_console()
        
        self.dormir += random.randint(0, 2)
        self.aburrimiento += random.randint(0, 3)
        self.hambre += random.randint(0, 4)
        self.limpieza += random.randint(0, 1)

        print("Para salir presione [x]")

        if self.dormir >= 100:
            print("¡Tu Tamagotchi está demasiado cansado! Necesita dormir.[d]")

        if self.aburrimiento >= 100:
            print("¡Tu Tamagotchi está muy aburrido! Dale algo para entretenerse.[e]")

        if self.hambre >= 100:
            print("¡Tu Tamagotchi está hambriento! Aliméntalo.[a]")
        
        if self.limpieza >= 100:
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
        pet = {"nombre": self.name, "dificultad": self.dificultad ,"d":self.dormir , "e":self.aburrimiento , "h": self.hambre,"l":self.limpieza}
        file = "pets\\pets.json"
        pets = {}
        
        if os.path.exists(file):
            with open(file, "r") as file_json:
                pets = json.load(file_json)

        pets.update(pet)

        with open(file, "w") as archivo_json:
            json.dump(pets, archivo_json, indent=4)

        self.animacionSaved()
