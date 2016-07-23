# Copyright (C) 2016 Ross D Milligan
# GNU GENERAL PUBLIC LICENSE Version 3 (full notice can be found at https://github.com/rdmilligan/PyMovieStudio)

from constants import *
from tracking import Tracking
from time import sleep
from random import randint

class Effects:

    # fog constants
    FOG_START_LOWER = 0.0
    FOG_START_UPPER = 10.0
    FOG_START_SHIFT = 0.5
    FOG_START_SHIFT_DELAY = 2

    # initialise
    def __init__(self, config_provider, disk, display, graphics):
        self.config_provider = config_provider
        self.disk = disk
        self.display = display
        self.graphics = graphics

        # clear log on disk
        self.disk.clear_log(self.config_provider.effects_save_to, EFFECTS_LOG_FILENAME)

        # tracking
        self.tracking = None
        if self.config_provider.effects_tracking:
            self.tracking = Tracking()

        # fog start
        self.fog_start = self._get_fog_start()

    # get fog start
    def _get_fog_start(self):
        
        # fog start
        fog_start = self.config_provider.effects_fog_start

        # ensure fog start within bounds
        if (fog_start <= self.FOG_START_LOWER) or (fog_start >= self.FOG_START_UPPER):
            return None

        return fog_start

    # add special effects to frame
    def frame(self, frame_number):

        # apply frame delay
        sleep(self.config_provider.frame_delay)

        # load frame from disk
        frame = self.disk.load_frame(self.config_provider.effects_load_from, None, frame_number, self.config_provider.frame_format)

        # ensure frame loaded from disk
        if frame is None:
            return False

        # track frame
        if self.tracking:
            frame = self.tracking.frame(frame)

        # apply fog
        if self.fog_start:
            self.fog_start = self._handle_fog_start(self.fog_start)
            self.graphics.fog(self.fog_start)

            # save log to disk
            self.disk.save_log("{},{}".format(frame_number, self.fog_start), self.config_provider.effects_save_to, EFFECTS_LOG_FILENAME)

        # display frame
        if self.config_provider.effects_display_frame:
            self.display.frame(frame)

        # save frame to disk
        self.disk.save_frame(frame, self.config_provider.effects_save_to, None, frame_number, self.config_provider.frame_format)

        return True

    # handle fog start
    def _handle_fog_start(self, fog_start):

            # determine whether to adjust fog start 
            if randint(0, self.FOG_START_SHIFT_DELAY) != 0:
                return fog_start

            # randomly increase or decrease fog start
            updated_fog_start = None

            if randint(0, 1) == 0:
                updated_fog_start = fog_start + self.FOG_START_SHIFT
            else:
                updated_fog_start = fog_start - self.FOG_START_SHIFT

            # ensure fog start does not breach its bounds
            if (updated_fog_start <= self.FOG_START_LOWER) or (updated_fog_start >= self.FOG_START_UPPER):
               return fog_start 

            return updated_fog_start