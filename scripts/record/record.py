# Copyright (C) 2016 Ross D Milligan
# GNU GENERAL PUBLIC LICENSE Version 3 (full notice can be found at https://github.com/rdmilligan/PyMovieStudio)

from webcam import Webcam
import cv2

class Record:

    # initialise
    def __init__(self, config_provider, disk):
        self.config_provider = config_provider
        self.disk = disk

        # cameras
        self.cameras = self._create_cameras()
        self._start_cameras()

    # create cameras
    def _create_cameras(self):

        cameras = []

        for camera_number in range(self.config_provider.number_of_cameras):
            cameras.append(Webcam(camera_number))

        return cameras

    # start cameras
    def _start_cameras(self):

        for camera_number in range(self.config_provider.number_of_cameras):
            self.cameras[camera_number].start()

    # record frames
    def frame(self, frame_number):

        # for each camera...
        for camera_number in range(self.config_provider.number_of_cameras):

            # ...get camera frame
            camera = self.cameras[camera_number]
            frame = camera.get_current_frame()

            # ensure frame fetched from camera
            if frame is None:
                return False

            # show frame
            if self.config_provider.record_show_frames:
                cv2.imshow('Record: camera number {}'.format(camera_number), frame)
                cv2.waitKey(1)

            # save frame to disk
            self.disk.save_frame(frame, self.config_provider.record_save_to, camera_number, frame_number, self.config_provider.frame_format)

        return True
