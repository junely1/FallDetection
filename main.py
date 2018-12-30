from imutils.video import VideoStream
import argparse
import datetime
import imutils
import time
import cv2
import queue
import numpy as np
import send_alert
import frame_process
import algorithm_fall

# argument parser creation
ap = argparse.ArgumentParser()

ap.add_argument("-v", "--video", help="path to the vidoe file")
ap.add_argument("-a", "--min-area", type=int, default=1500, help="minimum area size")

args = vars(ap.parse_args())

xList = queue.Queue(maxsize=10)
yList = queue.Queue(maxsize=10)
prevX =0.0
prevY=0.0
centerV = 0
centerSpeed = 0
alert = 0

if args.get("video", None) is None:
    #
    vs = VideoStream(src=0).start()
    time.sleep(2.0)

# we can also grab video and test
else:
    vs = cv2.VideoCapture(args["video"])

firstFrame = None

while True:
    
    frame = vs.read()
    frame = frame if args.get("video", None) is None else frame[1]
    text = ""
    
    if frame is None:
        break
    frame = imutils.resize(frame, width=500)
    gray = frame_process.preprocess_frame(frame)

    if firstFrame is None:
        firstFrame = gray
        continue

    frameDelta = cv2.absdiff(firstFrame, gray)

    cnts = frame_process.get_contours(firstFrame, gray)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]
    
    defined_min_area = args["min_area"]
    alert = algorithm_fall.fall_detect(cnts, defined_min_area, frame, prevX, prevY, xList, yList, centerV, alert)

    cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
        (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (255, 255, 255), 1)
    cv2.imshow("Frame Delta", frameDelta)
    cv2.imshow("Security Feed", frame)
    
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

vs.stop() if args.get("video", None) is None else vs.release()
cv2.destroyAllWindows()
