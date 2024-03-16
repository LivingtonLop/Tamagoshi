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
        self.eyes_open = True

    def live(self):
        self.clear_console()
        
        self.dormir += random.randint(0, 2)
        self.aburrimiento += random.randint(0, 3)
        self.hambre += random.randint(0, 4)
        self.limpieza += random.randint(0, 1)

        if self.dormir >= 10:
            print("¡Tu Tamagotchi está demasiado cansado! Necesita dormir.[d]")
            self.dormir -= 1 if self.dormir < 15 else 0  
        
        if self.aburrimiento >= 10:
            print("¡Tu Tamagotchi está muy aburrido! Dale algo para entretenerse.[e]")
            self.aburrimiento -= 1 if self.aburrimiento < 15 else 0  

        if self.hambre >= 10:
            print("¡Tu Tamagotchi está hambriento! Aliméntalo.[a]")
            self.hambre -= 1 if self.hambre < 15 else 0  
        
        if self.limpieza >= 10:
            print("¡Tu Tamagotchi está sucio! Debes limpiarlo.[l]")
            self.limpieza -= 1 if self.limpieza < 15 else 0  
        
        if self.key_push():
            tecla = self.get_key()
            accion = self.acciones.get(tecla)
            accion()
        
        self.animacionNormal(self.eyes_open) #Esto tiene que salir de aqui (hacer un mapa para esto, para que las animaciones sean dinamicas y no estaticas )
        self.eyes_open = not self.eyes_open

        

    def dormirAnimacion(self):
        self.dormir = self.dormir - 10
        #animacion dormir

    def limpiarAnimacion(self):
        self.limpieza = self.limpieza - 10
        print("limpiar...zzz") #animacion

    def alimentarAnimacion(self):
        self.hambre = self.hambre - 10
        print("alimentar...zzz") #animacion

    def entretenerAnimacion(self):
        self.aburrimiento = self.aburrimiento - 10
        print("entretener...zzz") #animacion

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
