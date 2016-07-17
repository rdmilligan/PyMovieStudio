# Copyright (C) 2016 Ross D Milligan
# GNU GENERAL PUBLIC LICENSE Version 3 (full notice can be found at https://github.com/rdmilligan/PyMovieStudio)

from OpenGL.GL import *

class Graphics:

    # apply fog
    def fog(self, fog_intensity):
        glFogi(GL_FOG_MODE, GL_LINEAR)
        glFogfv(GL_FOG_COLOR, (fog_intensity, fog_intensity, fog_intensity, 1.0))
        glHint(GL_FOG_HINT, GL_NICEST)
        glFogf(GL_FOG_START, 1.0)
        glFogf(GL_FOG_END, 12.0)
        glEnable(GL_FOG)



