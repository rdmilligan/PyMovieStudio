# Copyright (C) 2016 Ross D Milligan
# GNU GENERAL PUBLIC LICENSE Version 3 (full notice can be found at https://github.com/rdmilligan/PyMovieStudio)

from time import sleep
from random import randint
from pygame import mixer
import cv2

class Audio:

    # initialise
    def __init__(self, config_provider, disk):
        self.config_provider = config_provider
        self.disk = disk
        
        # clear log on disk
        self.disk.clear_log(self.config_provider.audio_save_to)

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

        # apply sound delay
        if randint(0, self.config_provider.audio_sound_delay) == 0:
            
            # play sound
            mixer.Sound("{}{}".format(self.config_provider.audio_save_to, self.config_provider.audio_sound_file)).play()
            
            # save log to disk
            self.disk.save_log("{},{}".format(frame_number, self.config_provider.audio_sound_file), self.config_provider.audio_save_to)

        # show frame
        if self.config_provider.audio_show_frame:
            cv2.imshow('Audio: camera', frame)
            cv2.waitKey(1)

        # save frame to disk
        self.disk.save_frame(frame, self.config_provider.audio_save_to, None, frame_number, self.config_provider.frame_format)

        return True