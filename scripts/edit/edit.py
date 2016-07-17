# Copyright (C) 2016 Ross D Milligan
# GNU GENERAL PUBLIC LICENSE Version 3 (full notice can be found at https://github.com/rdmilligan/PyMovieStudio)

from speech import Speech
from time import sleep

class Edit:

    # initialise
    def __init__(self, config_provider, disk, display):
        self.config_provider = config_provider
        self.disk = disk
        self.display = display

        # cameras
        self.cameras = self._create_cameras()
        self.camera_number = 0

        # speech recognition
        self.speech = Speech()
        self.speech.start()

    # create cameras
    def _create_cameras(self):

        # note: configure camera names to match speech recognition 
        camera_names = self.config_provider.edit_camera_names.split(',')

        cameras = []

        for camera_number in range(self.config_provider.number_of_cameras):
            cameras.append(camera_names[camera_number])

        return cameras

    # edit frame
    def frame(self, frame_number):

        # get camera name using speech recognition
        camera_name = self.speech.get_current_speech()

        # get camera number from camera name
        if camera_name in self.cameras:
            self.camera_number = self.cameras.index(camera_name) 

        # apply frame delay
        sleep(self.config_provider.frame_delay)

        # load frame from disk
        frame = self.disk.load_frame(self.config_provider.edit_load_from, self.camera_number, frame_number, self.config_provider.frame_format)

        # ensure frame loaded from disk
        if frame is None:
            return False

        # display frame
        if self.config_provider.edit_display_frame:
            self.display.frame(frame)

        # save frame to disk
        self.disk.save_frame(frame, self.config_provider.edit_save_to, None, frame_number, self.config_provider.frame_format)

        return True

