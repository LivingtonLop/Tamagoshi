from my_class.bienvenida import Bienvenida
from my_class.tamagoshi import Tamagoshi

#bucle para correr el programa (temporal)

welcome = Bienvenida()
Datos = None

Datos = welcome.bienvenido()


if type(Datos) is list:

    #nuevo bucle to el game
    pet =  Tamagoshi(petName=Datos[0],dificultadPet=Datos[1])

    if len(Datos) > 2: 
        pet =  Tamagoshi(petName=Datos[0],dificultadPet=Datos[1],domir=Datos[2],aburrimiento=Datos[3],hambre=Datos[4],limpieza=Datos[5])

    while True:
        pet.live()

