import time

from .animation import Animation

class AnimacionPet(Animation):

    scene_normal = "animations_ascii/pet_normal"
    scene_normal2 = "animations_ascii/pet_normal2"
    scene_died = "animations_ascii/pet_died"
    scene_died2 = "animations_ascii/game_over"

    def __init__(self):
        super().__init__()

    def animation_normal(self, mov: bool):
        if mov:
            print(self.find_scene(self.scene_normal))
        else:
            print(self.find_scene(self.scene_normal2))

        time.sleep(1)

    def animation_died(self):
        self.clear_console()
        print(self.find_scene(self.scene_died))
        print("You pet this death :( !!")
        time.sleep(3)

        self.clear_console()
        print(self.find_scene(self.scene_died2))
        time.sleep(3)
        
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

    def animacion_saved(self):
        print("Want u Exit? [yes] or [no] (please Write)")
        if input() == "yes":
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
