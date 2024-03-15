from my_class.bienvenida import Bienvenida
from my_class.tamagoshi import Tamagoshi


#bucle para correr el programa (temporal)

welcome = Bienvenida()


while True:
    Datos = welcome.bienvenido()

    if type(Datos) is list:
        break

#nuevo bucle to el game
pet =  Tamagoshi(petName=Datos[0],dificultadPet=Datos[1])

eyes_open = True

while True:
    pet.live()
    pet.animacionNormal(eyes_open)
    eyes_open = not eyes_open