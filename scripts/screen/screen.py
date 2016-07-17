# Copyright (C) 2016 Ross D Milligan
# GNU GENERAL PUBLIC LICENSE Version 3 (full notice can be found at https://github.com/rdmilligan/PyMovieStudio)

from constants import *
from pygame import mixer
from time import sleep

class Screen:

    # initialise
    def __init__(self, config_provider, disk, display, graphics):
        self.config_provider = config_provider
        self.disk = disk
        self.display = display
        self.graphics = graphics

        # effects
        self.effects_log = self.disk.load_log(self.config_provider.screen_load_from, EFFECTS_LOG_FILENAME)

        # audio
        self.audio_log = self.disk.load_log(self.config_provider.screen_load_from, AUDIO_LOG_FILENAME)
        mixer.init()

    # screen frame
    def frame(self, frame_number):

        # apply frame delay
        sleep(self.config_provider.frame_delay)

        # load frame from disk
        frame = self.disk.load_frame(self.config_provider.screen_load_from, None, frame_number, self.config_provider.frame_format)

        # ensure frame loaded from disk
        if frame is None:
            return False

        # handle effects
        self._handle_effects(frame_number)

        # handle audio
        self._handle_audio(frame_number)

        # display frame
        self.display.frame(frame)

        return True

    # handle effects
    def _handle_effects(self, frame_number):

        # loop effects log
        for item in self.effects_log:

            # extract frame number 
            item_parts = item.split(',')
            item_frame_number = int(item_parts[0])

            # apply fog intensity if frames match
            if item_frame_number == frame_number:
                item_fog_intensity = float(item_parts[1].replace('\n', ''))
                self.graphics.fog(item_fog_intensity)
                break

    # handle audio
    def _handle_audio(self, frame_number):

        # loop audio log
        for item in self.audio_log:

            # extract frame number 
            item_parts = item.split(',')
            item_frame_number = int(item_parts[0])

            # play sound if frames match
            if item_frame_number == frame_number:
                item_sound_file = item_parts[1].replace('\n', '')
                mixer.Sound("{}{}".format(self.config_provider.screen_load_from, item_sound_file)).play()
                break
        




