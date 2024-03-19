import time

from .animation import Animation

class AnimationSleep(Animation):
    scene_sleep = "animations_ascii/pet_sleep"
    scene_sleep2 = "animations_ascii/pet_sleep2"

    def __init__(self):
        super().__init__()

    def animation_sleep(self):
        
        frame1 = self.find_scene(self.scene_sleep)
        frame2 = self.find_scene(self.scene_sleep2)
        
        animation = self.animation_frame(frame1,frame2)
        
        for frame in animation:
            for line in frame:
                self.clear_console()
                print("Sleep ... shhh!")
                print (line)

            time.sleep(1)

        print("Woke up!")
        time.sleep(2)
    