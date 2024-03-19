import time

from .animacion import Animacion

class AnimacionPet(Animacion):
    scene = "animations_ascii/petnormal"
    scene2 = "animations_ascii/petnormal2"
    died = "animations_ascii/petmuerto"
    died2 = "animations_ascii/gameover"
    def __init__(self):
        super().__init__()

    def animacionNormal(self, mov: bool):
        if mov:
            print(self.findScene(self.scene))
        else:
            print(self.findScene(self.scene2))

        time.sleep(1)

    def died_animacion(self):
        self.clear_console()
        print(self.findScene(self.died))
        print("Ha muerto tu mascota :( !!")
        time.sleep(3)

        self.clear_console()
        print(self.findScene(self.died2))
        time.sleep(3)

        self.animacionSaved()

    def animacionSaved(self):
        self.clear_console()
        print(
            """
╔════════════════════════════════════╗
║                                    ║
║                                    ║
║                                    ║
║            GOOD BYA!!              ║
║                                    ║
║                                    ║
║                                    ║
╚════════════════════════════════════╝
            """
        )
        time.sleep(2)
        exit()
