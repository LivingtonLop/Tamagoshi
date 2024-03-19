from my_class.welcome import Welcome
from my_class.tamagotchi import Tamagotchi


welcome = Welcome()
data = None

data = welcome.welcome_init()

if type(data) is list:

    pet =  Tamagotchi(pet_name=data[0],pet_difficulty=data[1])

    if len(data) > 2: 
        pet =  Tamagotchi(pet_name=data[0],pet_difficulty=data[1],sleep=data[2],play=data[3],eat=data[4],clear=data[5])

    while True:
        pet.pet_live()
