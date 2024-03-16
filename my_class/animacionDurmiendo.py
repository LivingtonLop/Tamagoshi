import time

from .animacion import Animacion

class animacionDurmiendo(Animacion):
    scened = "animations_ascii/petdurmiendo"
    scened2 = "animations_ascii/petdurmiendo2"

    def __init__(self):
        super().__init__()

    def animacionDurmiendo(self):
        
        frame1 = self.findScene(self.scened)
        frame2 = self.findScene(self.scened2)
        
        animacion = self.animacionFrame(frame1,frame2)
        
        for frame in animacion:
            for linea in frame:
                self.clear_console()
                print("Durmiendo ... shhh!")
                print (linea)

            time.sleep(1)

        print("Se desperto!")
        time.sleep(2)
    