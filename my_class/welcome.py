import time
import os
import json

from .manager_key import ManagerKey

class Welcome (ManagerKey):

    scene_welcome = "animations_ascii/welcome"
    scene_welcome2 = "animations_ascii/difficulty"
    scene_resume = "animations_ascii/resumen"
    
    def __init__(self):
        super().__init__()
        
    def get_pet_name(self):
        print("\nPlease, Input name of you pet: ")
        pet_name = input()
        return pet_name

    def get_difficulty(self):
        print(self.find_scene(self.scene_welcome2))        

        difficulty = input("\nSelect Difficulty (1/2/3): ")
        return difficulty

    def welcome_init(self) -> list:
        data = self.saved_game()

        print(self.find_scene(self.scene_welcome))  
        if type(data) is list:
            print(f"Pets Saved [c] : {data[0]}")
            print("New Pet [n]")
            print("To exit push [x]")

            while not self.key_push():
                key = self.get_key()
                action = self.actions_welcome.get(key)
                if action is not None: return action()

        else:
            
            return self.pet_new()
        

    def saved_game(self) -> list:

        file = "pets\\pets.json"
        pets = {}
        if os.path.exists(file):
            with open(file, "r") as file_json:
                pets = json.load(file_json)

        return list(pets.values()) if len(list(pets.values())) > 0 else False
    
    def pet_new(self) -> list:
        pet_name = self.get_pet_name()

        if pet_name:
            self.clear_console()
            time.sleep(0.5)
            difficulty = self.get_difficulty()

            difficulty_text = {
                    "1":"Easy",
                    "2":"Medio",
                    "3":"Hard"
                }

            if difficulty:
                self.clear_console()
                time.sleep(0.5)
                    
                print(self.find_scene(self.scene_resume).format(pet_name = pet_name,difficulty_text =difficulty_text[difficulty]))

                time.sleep(5)
                
        return [pet_name, difficulty]

    def continue_pet(self) -> list:
        return self.saved_game()