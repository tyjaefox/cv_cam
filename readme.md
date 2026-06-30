### CV Camera Recognition Utility ###

# About

A basic camera recognition program written in Python. 

There are two different detector variations, a template and an orb detector.
    - Able to switch between the two by changing the 'detector' variable in main.py. (Make sure to change the text when calling `show_frame()` )

In the current public release, the program can only detect simple objects. I have been using a soda can for testing (image included in files)
    - This can be replaced with any clear image of a simple object. Be sure to change file name in .py files. 

# Purpose

Working base template for DIY security camera configuration. 

# Dependencies: 
    
- Python
- OpenCV
- numpy
- matplotlib

# Future Plans - Not Yet Implemented
 
- Multi-cam input/UI support

- Multi-image processing for simplicity and speed if used to detect a specific object, rather than vastly different variations of the same shape ( i.e. humans)

- YOLO detector/ Homgenous detector tests

- Footage and GUI casting to secondary device, such as tablets or standalone monitors.

- Detection training for human silhouettes and faces




