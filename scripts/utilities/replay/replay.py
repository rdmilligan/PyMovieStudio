# Copyright (C) 2016 Ross D Milligan
# GNU GENERAL PUBLIC LICENSE Version 3 (full notice can be found at https://github.com/rdmilligan/PyMovieStudio)

import cv2
from constants import *

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
    def effects(self, frame_number, disk, graphics, load_from, save_to):

        # load log
        effects_log = disk.load_log(load_from, EFFECTS_LOG_FILENAME)

        # loop log
        for item in effects_log:

            # extract frame number 
            item_parts = item.split(',')
            item_frame_number = int(item_parts[0])

            if item_frame_number < frame_number: continue
            if item_frame_number > frame_number: break

            # extract effects name
            item_effects_name = item_parts[1]

            # apply fog
            if item_effects_name == EFFECTS_NAME_FOG:
                item_fog_start = float(item_parts[2].replace('\n', ''))
                graphics.fog(item_fog_start)

                # save log to disk
                if save_to:
                    disk.save_log("{},{},{}".format(frame_number, EFFECTS_NAME_FOG, item_fog_start), save_to, EFFECTS_LOG_FILENAME)

            # apply lighting
            elif item_effects_name == EFFECTS_NAME_LIGHTING:
                item_enabled = int(item_parts[2].replace('\n', ''))
                graphics.lighting(item_enabled == 1)

                # save log to disk
                if save_to:
                    disk.save_log("{},{},{}".format(frame_number, EFFECTS_NAME_LIGHTING, item_enabled), save_to, EFFECTS_LOG_FILENAME)

            # apply blood
            if item_effects_name == EFFECTS_NAME_BLOOD:
                item_x_coord = item_parts[2]
                item_y_coord = item_parts[3].replace('\n', '')

                if item_x_coord == 'None' or item_y_coord == 'None':
                    item_x_coord = None
                    item_y_coord = None
                else:
                    item_x_coord = float(item_x_coord)
                    item_y_coord = float(item_y_coord)

                graphics.blood(item_x_coord, item_y_coord)

                # save log to disk
                if save_to:
                    disk.save_log("{},{},{},{}".format(frame_number, EFFECTS_NAME_BLOOD, item_x_coord, item_y_coord), save_to, EFFECTS_LOG_FILENAME)

    # audio
    def audio(self, frame_number, disk, mixer, load_from):

        # load log
        audio_log = disk.load_log(load_from, AUDIO_LOG_FILENAME)

        # loop log
        for item in audio_log:

            # extract frame number 
            item_parts = item.split(',')
            item_frame_number = int(item_parts[0])

            if item_frame_number < frame_number: continue
            if item_frame_number > frame_number: break

            # play sound
            item_sound_file = item_parts[1].replace('\n', '')
            mixer.Sound("{}{}".format(load_from, item_sound_file)).play()