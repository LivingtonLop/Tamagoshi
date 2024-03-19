#hereda todas las animaciones (Dormir, Alimentarse, Entreternerse y Limpiar)
import msvcrt
import json
import os
import random
import sys

from .animacionNomal import AnimacionPet
from .animacionDurmiendo import animacionDurmiendo
from .animacionComiendo import animacionComiendo
from .animacionJugando import animacionJugando
from .animacionLimpiando import animacionLimpiando 

class ManagerKey(AnimacionPet, animacionDurmiendo, animacionLimpiando, animacionComiendo, animacionJugando):
    def __init__(self):
        super().__init__()
        self.acciones = {
            "a" : lambda : self.alimentarAnimacion(),
            "e" : lambda : self.entretenerAnimacion(),
            "d" : lambda : self.dormirAnimacion(),
            "l" : lambda : self.limpiarAnimacion(),
            "s": lambda : self.savePet(),
            "x" : lambda : self.animacionSaved()
        }

        self.acciones_bienvenida = {
            "n" : lambda : self.nuevaPet(),
            "c" : lambda : self.continuarPet(),
            "x" : lambda : self.animacionSaved()
        }

        self.porcentajes = {
            "1": 30,
            "2":60,
            "3":90
        }

    def key_push(self):
        return msvcrt.kbhit()
    
    def get_key(self):
        return msvcrt.getch().decode('utf-8')
        
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

    def verificar_muerte(self,probabilidad_muerte) -> bool:
        numero_aleatorio = random.random()
        
        if numero_aleatorio <= probabilidad_muerte:
            return True
        else:
            return False

