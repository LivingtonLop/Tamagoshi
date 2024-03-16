#hereda todas las animaciones (Dormir, Alimentarse, Entreternerse y Limpiar)
import msvcrt
from .animacionDurmiendo import animacionDurmiendo
from .animacionComiendo import animacionComiendo
from .animacionJugando import animacionJugando
from .animacionLimpiando import animacionLimpiando 

class ManagerKey(animacionDurmiendo, animacionLimpiando, animacionComiendo, animacionJugando):
    def __init__(self):
        super().__init__()
        self.acciones = {
            "a" : self.alimentarAnimacion,
            "e" : self.entretenerAnimacion,
            "d" : self.dormirAnimacion,
            "l" : self.limpiarAnimacion,
            "s": self.savePet
        }

    def key_push(self):
        return msvcrt.kbhit()
    
    def get_key(self):
        return msvcrt.getch().decode('utf-8')