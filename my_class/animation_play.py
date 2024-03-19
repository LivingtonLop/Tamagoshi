import time

from .animation import Animation

class AnimationPlay(Animation):
    scene_play = "animations_ascii/pet_play"
    scene_play2 = "animations_ascii/pet_play2"

    def __init__(self):
        super().__init__()

    def animation_play(self):
        
        frame1 = self.find_scene(self.scene_play)
        frame2 = self.find_scene(self.scene_play2)
        
        animation = self.animation_frame(frame1,frame2)
        
        for frame in animation:
            for line in frame:
                self.clear_console()
                print("Playing ... XD!")
                print (line)

            time.sleep(1)

        print("Stop playing!")
        time.sleep(2)
    