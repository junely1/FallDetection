# FallDetection

This is a Fall Detection program.

System Requirements:
- Python 3.6
- OpenCV 2
- imutils library

You can recreate the virtual environment of my setup:

conda env create -f environment.yml


This program doesn't require any GPU, so it will be fine with CPU ONLY on any computer.
Developed and tested on MAC OSX (Macbook pro i5 core).

main.py is the main file.
frame_process.py is for processing the video.
algorithm_fall.py is for analyse the video frame and detects fall.
send_alarm.py is responsible for email alerts.

Run:

python main.py -v ./vids/cam1.avi -a 4000

To run this program, go to the file directory on terminal and use the following line, where ./vids/cam1.avi is the video to be processed (you may change) and 4000 is the minimum area value (experimentally 4000 gave u the best result).


