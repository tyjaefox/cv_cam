from cv_utils.camera_config import (
    start_camera, 
    get_frame, 
    show_frame, 
    cleanup
)
from cv_utils.orb_detector import ORBDetector
import cv2

cap = start_camera()

detector = ORBDetector("celsius2.jpg")


while True: 
    
    frame = get_frame(cap)
    
    if frame is None: 
        break
    
    frame = detector.detect(frame)
    
    show_frame("Camera Feed", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    
cleanup(cap)