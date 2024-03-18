import os

class Animacion():
    def clear_console(self):
        #En Windows es nt y en linux es posix
        os.system("cls" if os.name == "nt" else "clear")
        
    def findScene(self, filename: str) -> str:
        try:
            with open(filename + ".txt", "r",encoding='utf-8') as file:
                animacion = file.read()
                return animacion
        except FileNotFoundError:
            return "NOT FOUND : 404 ERROR"

    def animacionFrame(self, frame1, frame2: str)-> list:
        return [
                    [frame1],
                    [frame2],
                    [frame1],
                    [frame2],
                    [frame1]
                ]


        
