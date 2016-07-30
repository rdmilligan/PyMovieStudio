# Copyright (C) 2016 Ross D Milligan
# GNU GENERAL PUBLIC LICENSE Version 3 (full notice can be found at https://github.com/rdmilligan/PyMovieStudio)

from OpenGL.GL import *

class Graphics:

    # initialise
    def __init__(self):
        self.is_fog_init = False
        self.is_lighting_init = False

    # apply fog
    def fog(self, fog_start):

        if not self.is_fog_init:
            glFogi(GL_FOG_MODE, GL_LINEAR)
            glFogfv(GL_FOG_COLOR, (0.5, 0.5, 0.5, 1.0))
            glHint(GL_FOG_HINT, GL_NICEST)
            glFogf(GL_FOG_END, 12.0)
            glEnable(GL_FOG)
            self.is_fog_init = True            

        glFogf(GL_FOG_START, fog_start)

    # apply lighting
    def lighting(self, is_enabled):

        if not self.is_lighting_init:
            glLightfv(GL_LIGHT0, GL_AMBIENT, (0.5, 0.5, 0.5, 1.0))
            glLightfv(GL_LIGHT0, GL_DIFFUSE, (1.0, 1.0, 1.0, 1.0))
            glLightfv(GL_LIGHT0, GL_POSITION, (0.0, 0.0, 2.0, 1.0))
            glEnable(GL_LIGHT0)
            self.is_lighting_init = True

        if is_enabled:
            glEnable(GL_LIGHTING)
        else:
            glDisable(GL_LIGHTING)



