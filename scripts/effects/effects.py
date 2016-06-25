# Copyright (C) 2016 Ross D Milligan
# GNU GENERAL PUBLIC LICENSE Version 3 (full notice can be found at https://github.com/rdmilligan/PyMovieStudio)

from tracking import Tracking
from time import sleep
import cv2

class Effects:

    # initialise
    def __init__(self, config_provider, disk):
        self.config_provider = config_provider
        self.disk = disk

        # tracking
        self.tracking = Tracking()

    # add special effects to frame
    def frame(self, frame_number):

        # apply load delay
        sleep(self.config_provider.load_delay)

        # load frame from disk
        frame = self.disk.load_frame(self.config_provider.effects_load_from, None, frame_number, self.config_provider.frame_format)

        # ensure frame loaded from disk
        if frame is None:
            return False

        # track frame
        frame = self.tracking.frame(frame)

        # show frame
        if self.config_provider.effects_show_frame:
            cv2.imshow('Effects: camera', frame)
            cv2.waitKey(1)

        # save frame to disk
        self.disk.save_frame(frame, self.config_provider.effects_save_to, None, frame_number, self.config_provider.frame_format)

        return True