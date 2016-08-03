# Copyright (C) 2016 Ross D Milligan
# GNU GENERAL PUBLIC LICENSE Version 3 (full notice can be found at https://github.com/rdmilligan/PyMovieStudio)

from particle import Particle
from random import uniform
from OpenGL.GL import *

class ParticleSystem:

    # constants
    NUMBER_OF_PARTICLES = 100

    # initialise
    def __init__(self, x_coord, y_coord):
        self.particles = self._init_particles(x_coord, y_coord)
        self.active = True

    # initialise particles
    def _init_particles(self, x_coord, y_coord):
        particles = [Particle() for i in range(self.NUMBER_OF_PARTICLES)]

        # for each particle
        for particle in particles:

            # active settings
            particle.active = True
            particle.life = 1.0
            particle.ageing = uniform(0.1, 0.4)

            # colour
            particle.red = uniform(0.6, 0.9)
            particle.green = 0.0
            particle.blue = 0.0
 
            # coordinates
            particle.x = x_coord
            particle.y = y_coord
            particle.z = 0.0   

            # velocity
            particle.xv = uniform(-0.08, 0.08)
            particle.yv = uniform(-0.08, 0.08)
            particle.zv = 0.2        

        return particles

    # apply blood
    def blood(self):
        has_active_particles = False        

        # for each particle
        for particle in self.particles:

            # if particle active
            if particle.active:
                has_active_particles = True

                # get coordinates of particle
                x = particle.x
                y = particle.y
                z = particle.z

                glPushMatrix()
                glTranslatef(0.0,0.0,-9.0)
                glPushAttrib(GL_CURRENT_BIT)

                # set colour of particle
                glColor3f(particle.red, particle.green, particle.blue)
                
                # draw particle
                VERTEX_POS = 0.012

                glBegin(GL_TRIANGLE_STRIP)
                glVertex3f(x+VERTEX_POS, y+VERTEX_POS, z)
                glVertex3f(x-VERTEX_POS, y+VERTEX_POS, z)
                glVertex3f(x+VERTEX_POS, y-VERTEX_POS, z)
                glVertex3f(x-VERTEX_POS, y-VERTEX_POS, z)
                glEnd() 

                # update particle with velocity
                particle.x += particle.xv
                particle.y += particle.yv
                particle.z += particle.zv

                # update particle's life
                particle.life -= particle.ageing
                
                if particle.life <= 0.0:
                    particle.active = False

                glPopAttrib()
                glPopMatrix()

            # check for active particles
            if not has_active_particles:
                self.active = False