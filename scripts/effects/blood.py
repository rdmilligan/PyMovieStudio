# Copyright (C) 2016 Ross D Milligan
# GNU GENERAL PUBLIC LICENSE Version 3 (full notice can be found at https://github.com/rdmilligan/PyMovieStudio)

from random import *
from constants import *

class Blood:

    # blood constants
    BLOOD_DELAY = 20

    # apply
    def apply(self, frame_number, disk, graphics, save_to):
        x_coord = None
        y_coord = None

        # determine whether to set blood coordinates
        if randint(0, self.BLOOD_DELAY) == 0:
            x_coord = uniform(-1.0, 1.0)
            y_coord = uniform(-1.0, 1.0)

        # render blood
        graphics.blood(x_coord, y_coord)

        # save log to disk
        disk.save_log("{},{},{},{}".format(frame_number, EFFECTS_NAME_BLOOD, x_coord, y_coord), save_to, EFFECTS_LOG_FILENAME)