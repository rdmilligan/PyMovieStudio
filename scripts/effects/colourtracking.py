# Copyright (C) 2016 Ross D Milligan
# GNU GENERAL PUBLIC LICENSE Version 3 (full notice can be found at https://github.com/rdmilligan/PyMovieStudio)

from tracking import Tracking
import cv2

class ColourTracking(Tracking):

    # constants
    COLOUR_LOWER = (58,50,50)
    COLOUR_UPPER = (78,255,255)
    THRESHOLD = 1000

    # apply
    def apply(self, frame):

        # convert frame from BGR to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # only get colours in range
        mask = cv2.inRange(hsv, self.COLOUR_LOWER, self.COLOUR_UPPER)

        # obtain colour count
        colour_count = cv2.countNonZero(mask)

        # if threshold met...
        if colour_count > self.THRESHOLD:
            
            # handle mask
            frame = self.handle_mask(mask, frame)

        return frame