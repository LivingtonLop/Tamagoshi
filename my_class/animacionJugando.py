import time

from .animacion import Animacion

class animacionJugando(Animacion):
    scenej2 = "animations_ascii/petjugando"
    scenej22 = "animations_ascii/petjugando2"

    def __init__(self):
        super().__init__()

    def animacionJugando(self):
        
        frame1 = self.findScene(self.scenej2)
        frame2 = self.findScene(self.scenej22)
        
        animacion = self.animacionFrame(frame1,frame2)
        
        for frame in animacion:
            for linea in frame:
                self.clear_console()
                print("Jugando ... XD!")
                print (linea)

            time.sleep(1)

        print("Dejo de Jugar!")
        time.sleep(2)
    