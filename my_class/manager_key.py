#hereda todas las animaciones (Dormir, Alimentarse, Entreternerse y Limpiar)
import msvcrt
import json
import os
import random

from .animacion_normal import AnimacionPet
from .animation_sleep import AnimationSleep
from .animation_eat import AnimationEat
from .animation_play import AnimationPlay
from .animation_clear import AnimationLimpiando 

class ManagerKey(AnimacionPet, AnimationSleep, AnimationLimpiando, AnimationEat, AnimationPlay):
    def __init__(self):
        super().__init__()
        self.actions = {
            "e" : lambda : self.animation_eat(),
            "p" : lambda : self.animation_play(),
            "s" : lambda : self.animation_sleep(),
            "c" : lambda : self.animation_clear(),
            "g": lambda : self.save_pet(),
            "x" : lambda : self.animacion_saved()
        }

        self.actions_welcome = {
            "n" : lambda : self.pet_new(),
            "c" : lambda : self.continue_pet(),
            "x" : lambda : self.animacion_saved()
        }

        self.porcents = {
            "1": 30,
            "2":60,
            "3":90
        }

    def key_push(self):
        return msvcrt.kbhit()
    
    def get_key(self):
        return msvcrt.getch().decode('utf-8')
        
    def save_pet(self):
        pet = {"pet_name": self.pet_name, "difficulty": self.pet_difficulty ,"s":self.sleep , "p":self.play , "e": self.eat,"c":self.clear}
        file = "pets\\pets.json"
        pets = {}
        
        if os.path.exists(file):
            with open(file, "r") as file_json:
                pets = json.load(file_json)

        pets.update(pet)

        with open(file, "w") as archivo_json:
            json.dump(pets, archivo_json, indent=4)

        self.animacion_saved()

    def confirm_died(self,posibility_died) -> bool:
        number_aletory = random.random()
        
        if number_aletory <= posibility_died:
            return True
        else:
            return False

