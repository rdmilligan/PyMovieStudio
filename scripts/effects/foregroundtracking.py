# Copyright (C) 2016 Ross D Milligan
# GNU GENERAL PUBLIC LICENSE Version 3 (full notice can be found at https://github.com/rdmilligan/PyMovieStudio)

from tracking import Tracking
import cv2

class ForegroundTracking(Tracking):

    # initialise
    def __init__(self):
        
        # background subtraction
        self.backgroundSubtraction = cv2.BackgroundSubtractorMOG()

    # apply
    def apply(self, frame):

        # apply background subtraction
        mask = self.backgroundSubtraction.apply(frame, learningRate=1.0/12)

        # handle mask
        return self.handle_mask(mask, frame)