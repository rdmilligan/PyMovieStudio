# Copyright (C) 2016 Ross D Milligan
# GNU GENERAL PUBLIC LICENSE Version 3 (full notice can be found at https://github.com/rdmilligan/PyMovieStudio)

from constants import *
from foregroundtracking import ForegroundTracking
from colourtracking import ColourTracking
from fog import Fog
from blood import Blood
from time import sleep

class Effects:

    # initialise
    def __init__(self, config_provider, disk, display, graphics):
        self.config_provider = config_provider
        self.disk = disk
        self.display = display
        self.graphics = graphics

        # clear log on disk
        self.disk.clear_log(self.config_provider.effects_save_to, EFFECTS_LOG_FILENAME)

        # foreground tracking
        self.foreground_tracking = None
        if self.config_provider.effects_foreground_tracking:
            self.foreground_tracking = ForegroundTracking()

        # colour tracking
        self.colour_tracking = None
        if self.config_provider.effects_colour_tracking:
            self.colour_tracking = ColourTracking()

        # fog
        self.fog = None
        if self.config_provider.effects_fog:
            self.fog = Fog()

        # blood
        self.blood = None
        if self.config_provider.effects_blood:
            self.blood = Blood()

    # add special effects to frame
    def frame(self, frame_number):

        # apply frame delay
        sleep(self.config_provider.frame_delay)

        # load frame from disk
        frame = self.disk.load_frame(self.config_provider.effects_load_from, None, frame_number, self.config_provider.frame_format)

        # ensure frame loaded from disk
        if frame is None:
            return False

        # foreground tracking
        if self.foreground_tracking:
            frame = self.foreground_tracking.apply(frame)

        # colour tracking
        if self.colour_tracking:
            frame = self.colour_tracking.apply(frame, frame_number, self.disk, self.graphics, self.config_provider.effects_save_to)

        # fog
        if self.fog:
            self.fog.apply(frame_number, self.disk, self.graphics, self.config_provider.effects_save_to)

        # blood
        if self.blood:
            self.blood.apply(frame_number, self.disk, self.graphics, self.config_provider.effects_save_to)

        # display frame
        if self.config_provider.effects_display_frame:
            self.display.frame(frame)

        # save frame to disk
        self.disk.save_frame(frame, self.config_provider.effects_save_to, None, frame_number, self.config_provider.frame_format)

        return True