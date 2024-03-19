import time

from .animation import Animation

class AnimationEat(Animation):
    scene_eat = "animations_ascii/pet_eat"
    scene_eat2 = "animations_ascii/pet_eat2"

    def __init__(self):
        super().__init__()

    def animation_eat(self):
        
        frame1 = self.find_scene(self.scene_eat)
        frame2 = self.find_scene(self.scene_eat2)
        
        animation = self.animation_frame(frame1,frame2)
        
        for frame in animation:
            for line in frame:
                self.clear_console()
                print("Eating ... OWO!")
                print (line)

            time.sleep(1)

        print("Stop eat!")
        time.sleep(2)
    