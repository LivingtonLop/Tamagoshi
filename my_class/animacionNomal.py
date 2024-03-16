import time

from .animacion import Animacion

class AnimacionPet(Animacion):
    scene = "animations_ascii/petnormal"
    scene2 = "animations_ascii/petnormal2"
    died = "animations_ascii/petmuerto"

    def __init__(self):
        super().__init__()

    def animacionNormal(self, mov: bool):
        if mov:
            print(self.findScene(self.scene))
        else:
            print(self.findScene(self.scene2))

        time.sleep(1)