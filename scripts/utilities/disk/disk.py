# Copyright (C) 2016 Ross D Milligan
# GNU GENERAL PUBLIC LICENSE Version 3 (full notice can be found at https://github.com/rdmilligan/PyMovieStudio)

import cv2

class Disk:

    # load frame from disk
    def load_frame(self, path, camera_number, frame_number, frame_format):
        return cv2.imread(self._get_frame_disk_location(path, camera_number, frame_number, frame_format))

    # save frame to disk
    def save_frame(self, frame, path, camera_number, frame_number, frame_format):
        cv2.imwrite(self._get_frame_disk_location(path, camera_number, frame_number, frame_format), frame)

    # load log from disk
    def load_log(self, path, filename):
        log = []

        try:
            with open(self._get_log_disk_location(path, filename)) as log_file:
                log = log_file.readlines()
        except:
            print "Unable to load log"

        return log

    # save log to disk
    def save_log(self, log_text, path, filename):
        with open(self._get_log_disk_location(path, filename), "a") as log_file:
            log_file.write(log_text + '\n')

    # clear log on disk
    def clear_log(self, path, filename):
        open(self._get_log_disk_location(path, filename), 'w').close()

    # get frame disk location
    def _get_frame_disk_location(self, path, camera_number, frame_number, frame_format):

        camera_folder = ''
        
        if camera_number == None:
            camera_folder = 'camera/'
        else:
            camera_folder = 'camera_{}/'.format(camera_number)

        frame_name = 'frame_{}.{}'.format(frame_number, frame_format)

        return '{}{}{}'.format(path, camera_folder, frame_name)

    # get log disk location
    def _get_log_disk_location(self, path, filename):
        return "{}{}.txt".format(path, filename)









