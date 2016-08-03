# Copyright (C) 2016 Ross D Milligan
# GNU GENERAL PUBLIC LICENSE Version 3 (full notice can be found at https://github.com/rdmilligan/PyMovieStudio)

class Particle:

    # initialise
    def __init__(self):

        # active settings
        self.is_active = False
        self.life = 0.0
        self.ageing = 0.0

        # colour
        self.red = 0.0
        self.green = 0.0
        self.blue = 0.0

        # coordinates
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0

        # velocity
        self.xv = 0.0
        self.yv = 0.0
        self.zv = 0.0