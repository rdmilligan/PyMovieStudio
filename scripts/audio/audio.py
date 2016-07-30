# Copyright (C) 2016 Ross D Milligan
# GNU GENERAL PUBLIC LICENSE Version 3 (full notice can be found at https://github.com/rdmilligan/PyMovieStudio)

from constants import *
from pygame import mixer
from time import sleep
from random import randint

class Audio:

    # initialise
    def __init__(self, config_provider, disk, display, replay, graphics):
        self.config_provider = config_provider
        self.disk = disk
        self.display = display
        self.replay = replay
        self.graphics = graphics

        # clear logs on disk
        self.disk.clear_log(self.config_provider.audio_save_to, EFFECTS_LOG_FILENAME)
        self.disk.clear_log(self.config_provider.audio_save_to, AUDIO_LOG_FILENAME)

        # pygame mixer
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

        # replay effects
        self.replay.effects(frame_number, self.disk, self.graphics, self.config_provider.audio_load_from, self.config_provider.audio_save_to)

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