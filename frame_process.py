# frame.py : gets the frame and preprocesses for background subtraction

import time
import cv2
from imutils.video import VideoStream

def preprocess_frame(frame):
    
    # convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # use gaussian blur to blur frame
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
    return gray


def get_contours(firstFrame, gray):
    
    frameDelta = cv2.absdiff(firstFrame, gray)
    thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
    
    # dilate the thresholded image to fill in holes, then find contours
    # on thresholded image
    thresh = cv2.dilate(thresh, None, iterations=2)
    
    # contour detection to find the outlines of these white regions
    # filter out the small, irrelevant contours
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    return cnts


