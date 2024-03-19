import random

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
        self.vida = 100
        self.num_st = 100
        self.num_rest_st = 50
        self.num_t_st = 400

    def live(self):
        self.clear_console()
        self.dormir += random.randint(0, 2) #2
        self.aburrimiento += random.randint(0, 3) #2
        self.hambre += random.randint(0, 4) #1
        self.limpieza += random.randint(0, 1)#3

        print("Para salir presione [x]")
        print("Para Guardar Partida y salir [s]")

        if self.dormir >= self.num_st:
            print("¡Tu Tamagotchi está demasiado cansado! Necesita dormir.[d]")

        if self.aburrimiento >= self.num_st:
            print("¡Tu Tamagotchi está muy aburrido! Dale algo para entretenerse.[e]")

        if self.hambre >= self.num_st:
            print("¡Tu Tamagotchi está hambriento! Aliméntalo.[a]")
        
        if self.limpieza >= self.num_st:
            print("¡Tu Tamagotchi está sucio! Debes limpiarlo.[l]")
        
        if self.key_push():
            tecla = self.get_key()
            accion = self.acciones.get(tecla)
            accion()
        else:
            self.animacionNormal(mov=self.mov)

        self.mov = not self.mov

        self.diedTamagoshi()

    def dormirAnimacion(self):
        self.dormir -= self.num_rest_st
        self.animacionDurmiendo()

    def limpiarAnimacion(self):
        self.limpieza -= self.num_rest_st
        self.animacionLimpiando()

    def alimentarAnimacion(self):
        self.hambre -= self.num_rest_st
        self.animacionComiendo()

    def entretenerAnimacion(self):
        self.aburrimiento -= self.num_rest_st
        self.animacionJugando() 
        
    def diedTamagoshi(self):
        
        sumaT = self.aburrimiento + self.dormir + self.limpieza + self.hambre 

        if  sumaT >= self.num_t_st:
            indice = str(self.dificultad)
            porcentaje = self.porcentajes[indice]
            if self.verificar_muerte(porcentaje) : self.vida -= 1
        if self.vida == 0: 
            self.died_animacion()
        