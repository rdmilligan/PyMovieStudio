# Copyright (C) 2016 Ross D Milligan
# GNU GENERAL PUBLIC LICENSE Version 3 (full notice can be found at https://github.com/rdmilligan/PyMovieStudio)

import cv2

class Tracking:

    # handle mask
    def handle_mask(self, mask, frame):

        # get contours for objects in mask
        contours = self._get_contours(mask)
        if not contours: return frame

        # get largest contour
        contour = sorted(contours, key=cv2.contourArea, reverse=True)[0]

        # get centre coordinates of contour
        coord = self._get_contour_centroid(contour)

        # draw crosshairs at coordinates
        self._draw_crosshairs(frame, coord)

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

    # draw crosshairs
    def _draw_crosshairs(self, frame, coord):
        
        # set crosshairs colour
        crosshairs_colour = (0,0,255)

        # set crosshairs points
        top_point = (coord[0], coord[1] - 20)
        bottom_point = (coord[0], coord[1] + 20)
        left_point = (coord[0] - 20, coord[1])
        right_point = (coord[0] + 20, coord[1])

        # draw crosshairs
        cv2.circle(frame, coord, 12, crosshairs_colour, 2)
        cv2.line(frame, top_point, bottom_point, crosshairs_colour, 1)
        cv2.line(frame, left_point, right_point, crosshairs_colour, 1)