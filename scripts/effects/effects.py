# Copyright (C) 2016 Ross D Milligan
# GNU GENERAL PUBLIC LICENSE Version 3 (full notice can be found at https://github.com/rdmilligan/PyMovieStudio)

from constants import *
from tracking import Tracking
from time import sleep
from random import randint

class Effects:

    # fog constants
    FOG_INTENSITY_LOWER = 0.0
    FOG_INTENSITY_UPPER = 1.0
    FOG_INTENSITY_SHIFT = 0.01

    # initialise
    def __init__(self, config_provider, disk, display, graphics):
        self.config_provider = config_provider
        self.disk = disk
        self.display = display
        self.graphics = graphics

        # clear log on disk
        self.disk.clear_log(self.config_provider.effects_save_to, EFFECTS_LOG_FILENAME)

        # tracking
        self.tracking = Tracking()

        # fog intensity
        self.fog_intensity = self._get_fog_intensity()

    # get fog intensity
    def _get_fog_intensity(self):
        
        # fog intensity
        fog_intensity = self.config_provider.effects_fog_intensity

        # ensure fog intensity within bounds
        if (fog_intensity <= self.FOG_INTENSITY_LOWER) or (fog_intensity >= self.FOG_INTENSITY_UPPER):
            return None

        return fog_intensity

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
        frame = self.tracking.frame(frame)

        # apply fog intensity
        if self.fog_intensity:
            self.fog_intensity = self._handle_fog_intensity(self.fog_intensity, frame_number)
            self.graphics.fog(self.fog_intensity)

            # save log to disk
            self.disk.save_log("{},{}".format(frame_number, self.fog_intensity), self.config_provider.effects_save_to, EFFECTS_LOG_FILENAME)

        # display frame
        if self.config_provider.effects_display_frame:
            self.display.frame(frame)

        # save frame to disk
        self.disk.save_frame(frame, self.config_provider.effects_save_to, None, frame_number, self.config_provider.frame_format)

        return True

    # handle fog intensity
    def _handle_fog_intensity(self, fog_intensity, frame_number):

            # determine whether to adjust fog intensity 
            if randint(0, self.config_provider.effects_fog_delay) != 0:
                return fog_intensity

            # randomly increase or decrease fog intensity
            updated_fog_intensity = None

            if randint(0, 1) == 0:
                updated_fog_intensity = fog_intensity + self.FOG_INTENSITY_SHIFT
            else:
                updated_fog_intensity = fog_intensity - self.FOG_INTENSITY_SHIFT

            # ensure fog intensity does not breach its bounds
            if (updated_fog_intensity <= self.FOG_INTENSITY_LOWER) or (updated_fog_intensity >= self.FOG_INTENSITY_UPPER):
               return fog_intensity 

            return updated_fog_intensity