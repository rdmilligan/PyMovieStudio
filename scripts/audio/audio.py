# Copyright (C) 2016 Ross D Milligan
# GNU GENERAL PUBLIC LICENSE Version 3 (full notice can be found at https://github.com/rdmilligan/PyMovieStudio)

from constants import *
from pygame import mixer
from time import sleep
from random import randint

class Audio:

    # initialise
    def __init__(self, config_provider, disk, display, graphics):
        self.config_provider = config_provider
        self.disk = disk
        self.display = display
        self.graphics = graphics

        # clear logs on disk
        self.disk.clear_log(self.config_provider.audio_save_to, EFFECTS_LOG_FILENAME)
        self.disk.clear_log(self.config_provider.audio_save_to, AUDIO_LOG_FILENAME)

        # effects
        self.effects_log = self.disk.load_log(self.config_provider.audio_load_from, EFFECTS_LOG_FILENAME)

        # pygame audio
        mixer.init()

    # add audio to frame
    def frame(self, frame_number):

        # apply frame delay
        sleep(self.config_provider.frame_delay)

        # load frame from disk
        frame = self.disk.load_frame(self.config_provider.audio_load_from, None, frame_number, self.config_provider.frame_format)

        # ensure frame loaded from disk
        if frame is None:
            return False

        # handle effects
        self._handle_effects(frame_number)

        # apply sound delay
        if randint(0, self.config_provider.audio_sound_delay) == 0:
            
            # play sound
            mixer.Sound("{}{}".format(self.config_provider.audio_save_to, self.config_provider.audio_sound_file)).play()
            
            # save log to disk
            self.disk.save_log("{},{}".format(frame_number, self.config_provider.audio_sound_file), self.config_provider.audio_save_to, AUDIO_LOG_FILENAME)

        # display frame
        if self.config_provider.audio_display_frame:
            self.display.frame(frame)

        # save frame to disk
        self.disk.save_frame(frame, self.config_provider.audio_save_to, None, frame_number, self.config_provider.frame_format)

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

                # save log to disk
                self.disk.save_log("{},{}".format(frame_number, item_fog_intensity), self.config_provider.audio_save_to, EFFECTS_LOG_FILENAME)
                break