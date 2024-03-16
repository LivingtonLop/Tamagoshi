import time

from .animacion import Animacion

class animacionComiendo(Animacion):
    scenec2 = "animations_ascii/petcomiendo"
    scenec22 = "animations_ascii/petcomiendo2"

    def __init__(self):
        super().__init__()

    def animacionComiendo(self):
        
        frame1 = self.findScene(self.scenec2)
        frame2 = self.findScene(self.scenec22)
        
        animacion = self.animacionFrame(frame1,frame2)
        
        for frame in animacion:
            for linea in frame:
                self.clear_console()
                print("Comiendo ... OWO!")
                print (linea)

            time.sleep(1)

        print("Dejo de Comer!")
        time.sleep(2)
    