import random

from .manager_key import ManagerKey
class Tamagotchi(ManagerKey):

    def __init__(self, pet_name, pet_difficulty,sleep = 0, play = 0, eat = 0, clear = 0) -> None:
        super().__init__()
        self.pet_name = pet_name
        self.pet_difficulty = pet_difficulty
        #default
        self.sleep = sleep
        self.play = play
        self.eat = eat
        self.clear = clear
        self.mov = True
        self.health = 100
        self.number_limit_state = 100
        self.number_rest_state = 50
        self.number_sum_all_state = 400

    def pet_live(self):
        self.clear_console()
        self.sleep += random.randint(0, 2) 
        self.play += random.randint(0, 3) 
        self.eat += random.randint(0, 4) 
        self.clear += random.randint(0, 1)

        print("To exit push [x]")
        print("To saved & exit push [g]")

        if self.sleep >= self.number_limit_state:
            print(f"¡{self.pet_name} this very tired! Need sleep.[s]")

        if self.play >= self.number_limit_state:
            print(f"¡{self.pet_name} this very Bored! Give {self.pet_name} some to play.[p]")

        if self.eat >= self.number_limit_state:
            print(f"¡{self.pet_name} this with hungry! Give {self.pet_name} some to eat.[e]")
        
        if self.clear >= self.number_limit_state:
            print(f"¡{self.pet_name} this dirty! Needs cleaning.[c]")
        
        if self.key_push():
            key = self.get_key()
            action = self.actions.get(key)
            if action is not None: action()
        else:
            self.animation_normal(mov=self.mov)

        self.mov = not self.mov

        self.died_tamagoshi()

    def sleep_animation(self):
        self.sleep -= self.number_rest_state
        self.animation_sleep()

    def clear_animation(self):
        self.clear -= self.number_rest_state
        self.animation_clear()

    def eat_animation(self):
        self.eat -= self.number_rest_state
        self.animation_eat()

    def play_animation(self):
        self.play -= self.number_rest_state
        self.animation_play() 
        
    def died_tamagoshi(self):
        
        plusT = self.play + self.sleep + self.clear + self.eat 

        if  plusT >= self.number_sum_all_state:
            index = str(self.pet_difficulty)
            porcent = self.porcents[index]
            if self.confirm_died(porcent) : self.health -= 1
        if self.health == 0: 
            self.animation_died()
        