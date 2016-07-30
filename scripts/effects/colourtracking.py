# Copyright (C) 2016 Ross D Milligan
# GNU GENERAL PUBLIC LICENSE Version 3 (full notice can be found at https://github.com/rdmilligan/PyMovieStudio)

from tracking import Tracking
import cv2
from random import randint
from constants import *

class ColourTracking(Tracking):

    # constants
    COLOUR_LOWER = (58,50,50)
    COLOUR_UPPER = (78,255,255)
    THRESHOLD = 1000

    # apply
    def apply(self, frame, frame_number, disk, graphics, save_to):

        # convert frame from BGR to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # only get colours in range
        mask = cv2.inRange(hsv, self.COLOUR_LOWER, self.COLOUR_UPPER)

        # obtain colour count
        colour_count = cv2.countNonZero(mask)

        # if threshold met...
        lighting_enabled = 0
        if colour_count > self.THRESHOLD:
            
            # handle mask
            frame = self.handle_mask(mask, frame)
            
            # randomly switch lighting on or off
            if randint(0, 1) == 0:
                graphics.lighting(True)
                lighting_enabled = 1
            else:
                graphics.lighting(False)

        # otherwise...
        else:

            # switch lighting off
            graphics.lighting(False)

        # save log to disk
        disk.save_log("{},{},{}".format(frame_number, EFFECTS_NAME_LIGHTING, lighting_enabled), save_to, EFFECTS_LOG_FILENAME)

        return frame