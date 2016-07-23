# Copyright (C) 2016 Ross D Milligan
# GNU GENERAL PUBLIC LICENSE Version 3 (full notice can be found at https://github.com/rdmilligan/PyMovieStudio)

import cv2

class Replay:

    # record
    def record(self, frame_number, disk, number_of_cameras, load_from, frame_format):
        
        # for each camera...
        for camera_number in range(number_of_cameras):

            # load frame from disk
            frame = disk.load_frame(load_from, camera_number, frame_number, frame_format)

            # ensure frame loaded from disk
            if frame is None:
                return False

            # display frame
            cv2.imshow('Replay record: camera number {}'.format(camera_number), frame)
            cv2.waitKey(1)

    # effects
    def effects(self, frame_number, disk, graphics, load_from, save_to, filename):

        # load log
        effects_log = disk.load_log(load_from, filename)

        # loop log
        for item in effects_log:

            # extract frame number 
            item_parts = item.split(',')
            item_frame_number = int(item_parts[0])

            # apply fog start if frames match
            if item_frame_number == frame_number:
                item_fog_start = float(item_parts[1].replace('\n', ''))
                graphics.fog(item_fog_start)

                # save log to disk
                if save_to:
                    disk.save_log("{},{}".format(frame_number, item_fog_start), save_to, filename)

                break

    # audio
    def audio(self, frame_number, disk, mixer, load_from, filename):

        # load log
        audio_log = disk.load_log(load_from, filename)

        # loop log
        for item in audio_log:

            # extract frame number 
            item_parts = item.split(',')
            item_frame_number = int(item_parts[0])

            # play sound if frames match
            if item_frame_number == frame_number:
                item_sound_file = item_parts[1].replace('\n', '')
                mixer.Sound("{}{}".format(load_from, item_sound_file)).play()
                break