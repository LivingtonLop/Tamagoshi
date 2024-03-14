import os

class Animacion():
    def clear_console(self):
        #En Windows es nt y en linux es posix
        os.system("cls" if os.name == "nt" else "clear")

    def findScene(self):
        pass