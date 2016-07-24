# Copyright (C) 2016 Ross D Milligan
# GNU GENERAL PUBLIC LICENSE Version 3 (full notice can be found at https://github.com/rdmilligan/PyMovieStudio)

from random import randint

class Fog:

    # fog constants
    FOG_START_INITIAL = 5.0
    FOG_START_LOWER = 0.0
    FOG_START_UPPER = 10.0
    FOG_START_SHIFT = 0.5
    FOG_START_SHIFT_DELAY = 2

    # initialise
    def __init__(self):

        # fog start
        self.fog_start = self.FOG_START_INITIAL

    # get fog start
    def _get_fog_start(self):

            # determine whether to adjust fog start 
            if randint(0, self.FOG_START_SHIFT_DELAY) != 0:
                return self.fog_start

            # randomly increase or decrease fog start
            adjusted_fog_start = self.fog_start

            if randint(0, 1) == 0:
                adjusted_fog_start = self.fog_start + self.FOG_START_SHIFT
            else:
                adjusted_fog_start = self.fog_start - self.FOG_START_SHIFT

            # ensure fog start within its bounds
            if (adjusted_fog_start > self.FOG_START_LOWER) and (adjusted_fog_start < self.FOG_START_UPPER):
                self.fog_start = adjusted_fog_start

            return self.fog_start

    # apply
    def apply(self, graphics):

        # get fog start
        fog_start = self._get_fog_start()

        # render fog
        graphics.fog(fog_start)

        return fog_start