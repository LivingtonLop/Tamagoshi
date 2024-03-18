#hereda todas las animaciones (Dormir, Alimentarse, Entreternerse y Limpiar)
import msvcrt
from .animacionNomal import AnimacionPet
from .animacionDurmiendo import animacionDurmiendo
from .animacionComiendo import animacionComiendo
from .animacionJugando import animacionJugando
from .animacionLimpiando import animacionLimpiando 

class ManagerKey(AnimacionPet, animacionDurmiendo, animacionLimpiando, animacionComiendo, animacionJugando):
    def __init__(self):
        super().__init__()
        self.acciones = {
            "a" : lambda : self.alimentarAnimacion(),
            "e" : lambda : self.entretenerAnimacion(),
            "d" : lambda : self.dormirAnimacion(),
            "l" : lambda : self.limpiarAnimacion(),
            "s": lambda : self.savePet(),
            "x" : lambda : self.animacionSaved()
        }

        self.acciones_bienvenida = {
            "n" : lambda : self.nuevaPet(),
            "c" : lambda : self.continuarPet(),
            "x" : lambda : self.animacionSaved()
        }

    def key_push(self):
        return msvcrt.kbhit()
    
    def get_key(self):
        return msvcrt.getch().decode('utf-8')
        
    