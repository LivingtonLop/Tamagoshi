import time

from .animation import Animation

class AnimationLimpiando(Animation):
    scene_clear = "animations_ascii/pet_clear"
    scene_clear2 = "animations_ascii/pet_clear2"

    def __init__(self):
        super().__init__()

    def animation_clear(self):
        
        frame1 = self.find_scene(self.scene_clear)
        frame2 = self.find_scene(self.scene_clear2)
        
        animation = self.animation_frame(frame1,frame2)
        
        for frame in animation:
            for line in frame:
                self.clear_console()
                print("cleaning ... Uff!")
                print (line)

            time.sleep(1)

        print("Stop clear!")
        time.sleep(2)
    