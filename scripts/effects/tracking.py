# Copyright (C) 2016 Ross D Milligan
# GNU GENERAL PUBLIC LICENSE Version 3 (full notice can be found at https://github.com/rdmilligan/PyMovieStudio)

import cv2

class Tracking:

    # initialise
    def __init__(self):
        
        # background subtraction
        self.backgroundSubtraction = cv2.BackgroundSubtractorMOG()

    # track frame
    def frame(self, frame):

        # apply background subtraction
        fgmask = self.backgroundSubtraction.apply(frame, learningRate=1.0/12)

        # get contours for objects in foreground
        contours = self._get_contours(fgmask)
        if not contours: return frame

        # get largest contour
        contour = sorted(contours, key=cv2.contourArea, reverse=True)[0]

        # get centre coordinates of contour
        coord = self._get_contour_centroid(contour)

        # drawn circle at coordinates
        cv2.circle(frame, coord, 6, (0,0,255), -1)

        return frame

    # get contours from image
    def _get_contours(self, image):
        edges = cv2.Canny(image, 100, 200)
        contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        return contours
 
    # get contour centroid
    def _get_contour_centroid(self, contour):
        try:
            M = cv2.moments(contour)
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            return (cx, cy)
        except:
            return (0, 0)

