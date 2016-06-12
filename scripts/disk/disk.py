# Copyright (C) 2016 Ross D Milligan
# GNU GENERAL PUBLIC LICENSE Version 3 (full notice can be found at https://github.com/rdmilligan/PyMovieStudio)

import cv2

class Disk:

    # load frame from disk
    def load_frame(self, path, camera_number, frame_number, frame_format):
        return cv2.imread(self._get_disk_location(path, camera_number, frame_number, frame_format))

    # save frame to disk
    def save_frame(self, frame, path, camera_number, frame_number, frame_format):
        cv2.imwrite(self._get_disk_location(path, camera_number, frame_number, frame_format), frame)

    # get disk location
    def _get_disk_location(self, path, camera_number, frame_number, frame_format):

        camera_folder = ''
        
        if camera_number == None:
            camera_folder = 'camera/'
        else:
            camera_folder = 'camera_{}/'.format(camera_number)

        frame_name = 'frame_{}.{}'.format(frame_number, frame_format)

        return '{}{}{}'.format(path, camera_folder, frame_name)








