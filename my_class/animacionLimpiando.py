import time

from .animacion import Animacion

class animacionLimpiando(Animacion):
    scenel = "animations_ascii/petlimpiando"
    scenel2 = "animations_ascii/petlimpiando2"

    def __init__(self):
        super().__init__()

    def animacionLimpiando(self):
        
        frame1 = self.findScene(self.scenel)
        frame2 = self.findScene(self.scenel2)
        
        animacion = self.animacionFrame(frame1,frame2)
        
        for frame in animacion:
            for linea in frame:
                self.clear_console()
                print("Limpiando ... Uff!")
                print (linea)

            time.sleep(1)

        print("Dejo de Limpiarse!")
        time.sleep(2)
    