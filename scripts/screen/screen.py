# Copyright (C) 2016 Ross D Milligan
# GNU GENERAL PUBLIC LICENSE Version 3 (full notice can be found at https://github.com/rdmilligan/PyMovieStudio)

from constants import *
from pygame import mixer
from time import sleep

class Screen:

    # initialise
    def __init__(self, config_provider, disk, display, replay, graphics):
        self.config_provider = config_provider
        self.disk = disk
        self.display = display
        self.replay = replay
        self.graphics = graphics

        # pygame mixer
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

        # replay effects
        self.replay.effects(frame_number, self.disk, self.graphics, self.config_provider.screen_load_from, None)

        # replay audio
        self.replay.audio(frame_number, self.disk, mixer, self.config_provider.screen_load_from)

        # display frame
        self.display.frame(frame)

        return True
