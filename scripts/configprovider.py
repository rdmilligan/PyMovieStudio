# Copyright (C) 2016 Ross D Milligan
# GNU GENERAL PUBLIC LICENSE Version 3 (full notice can be found at https://github.com/rdmilligan/PyMovieStudio)

import ConfigParser

class ConfigProvider:

    def __init__(self):
        self.config = ConfigParser.ConfigParser()
        self.config.read('appsettings.ini')

    @property
    def record_enabled(self):
        return self.config.getboolean('Record', 'Enabled')

    @property
    def record_save_to(self):
        return self.config.get('Record', 'SaveTo')

    @property
    def record_show_frames(self):
        return self.config.getboolean('Record', 'ShowFrames')

    @property
    def edit_enabled(self):
        return self.config.getboolean('Edit', 'Enabled')

    @property
    def edit_load_from(self):
        return self.config.get('Edit', 'LoadFrom')

    @property
    def edit_save_to(self):
        return self.config.get('Edit', 'SaveTo')

    @property
    def edit_show_frame(self):
        return self.config.getboolean('Edit', 'ShowFrame')

    @property
    def edit_camera_names(self):
        return self.config.get('Edit', 'CameraNames')

    @property
    def screen_enabled(self):
        return self.config.getboolean('Screen', 'Enabled')

    @property
    def screen_load_from(self):
        return self.config.get('Screen', 'LoadFrom')

    @property
    def number_of_cameras(self):
        return self.config.getint('Shared', 'NumberOfCameras')

    @property
    def load_delay(self):
        return self.config.getfloat('Shared', 'LoadDelay')

    @property
    def frame_format(self):
        return self.config.get('Shared', 'FrameFormat')
