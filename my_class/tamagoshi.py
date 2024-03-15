import random
import json
import os

from .animacionNomal import AnimacionPet

class Tamagoshi(AnimacionPet):

    def __init__(self, petName, dificultadPet) -> None:
        super().__init__()
        self.name = petName
        self.dificultad = dificultadPet
        #default
        self.dormir = 0
        self.aburrimiento = 0
        self.hambre = 0
        self.limpieza = 0

    def live(self):
        self.clear_console()
        # Aumentar las variables de manera aleatoria
        self.dormir += random.randint(0, 2)
        self.aburrimiento += random.randint(0, 3)
        self.hambre += random.randint(0, 4)
        self.limpieza += random.randint(0, 1)

        # Verificar si alguna variable llega a 10 y mostrar un mensaje
        if self.dormir >= 10:
            print("¡Tu Tamagotchi está demasiado cansado! Necesita dormir.")
        if self.aburrimiento >= 10:
            print("¡Tu Tamagotchi está muy aburrido! Dale algo para entretenerse.")
        if self.hambre >= 10:
            print("¡Tu Tamagotchi está hambriento! Aliméntalo.")
        if self.limpieza >= 10:
            print("¡Tu Tamagotchi está sucio! Debes limpiarlo.")
        
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