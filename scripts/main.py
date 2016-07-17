# Copyright (C) 2016 Ross D Milligan
# GNU GENERAL PUBLIC LICENSE Version 3 (full notice can be found at https://github.com/rdmilligan/PyMovieStudio)

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from configprovider import ConfigProvider
from utilities import *
from record import Record
from edit import Edit
from effects import Effects
from audio import Audio
from screen import Screen

class PyMovieStudio:

    # initialise
    def __init__(self):
        
        # config
        self.config_provider = ConfigProvider()

        # disk
        self.disk = Disk()

        # display
        self.display = None
        if (self.config_provider.edit_enabled or self.config_provider.effects_enabled or
            self.config_provider.audio_enabled or self.config_provider.screen_enabled):
            self.display = Display()

        # graphics
        self.graphics = None
        if (self.config_provider.effects_enabled or self.config_provider.audio_enabled or
            self.config_provider.screen_enabled):
            self.graphics = Graphics()

        # record
        self.record = None
        if self.config_provider.record_enabled:
            self.record = Record(self.config_provider, self.disk)

        # edit
        self.edit = None
        if self.config_provider.edit_enabled:
            self.edit = Edit(self.config_provider, self.disk, self.display)

        # effects
        self.effects = None
        if self.config_provider.effects_enabled:
            self.effects = Effects(self.config_provider, self.disk, self.display, self.graphics)

        # audio
        self.audio = None
        if self.config_provider.audio_enabled:
            self.audio = Audio(self.config_provider, self.disk, self.display, self.graphics)

        # screen
        self.screen = None
        if self.config_provider.screen_enabled:
            self.screen = Screen(self.config_provider, self.disk, self.display, self.graphics)

        # frame number
        self.frame_number = 0 

    # initialise OpenGL
    def _init_opengl(self):
        glClearColor(0.0, 0.0, 0.0, 0.0)
        glClearDepth(1.0)
        glDepthFunc(GL_LESS)
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_SMOOTH)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(33.7, 1.3, 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)

        # display
        if self.display:
            self.display.init_opengl()

    # process frame
    def _process_frame(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        # record
        if self.record:
            if self.record.frame(self.frame_number) == False: return

        # edit
        if self.edit:
            if self.edit.frame(self.frame_number) == False: return

        # effects
        if self.effects:
            if self.effects.frame(self.frame_number) == False: return

        # audio
        if self.audio:
            if self.audio.frame(self.frame_number) == False: return

        # screen
        if self.screen:
            if self.screen.frame(self.frame_number) == False: return

        # increment frame number
        self.frame_number += 1

        glutSwapBuffers()

    def main(self):
        # setup and run OpenGL
        glutInit()
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
        glutInitWindowSize(640, 480)
        glutInitWindowPosition(100, 100)
        glutCreateWindow('PyMovieStudio')
        glutDisplayFunc(self._process_frame)
        glutIdleFunc(self._process_frame)
        self._init_opengl()
        glutMainLoop()

# run an instance of PyMovieStudio
pyMovieStudio = PyMovieStudio()
pyMovieStudio.main()