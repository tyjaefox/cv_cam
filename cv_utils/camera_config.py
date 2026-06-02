import cv2


# start camera feed

def start_camera(camera_index = 0):
    return cv2.VideoCapture(camera_index)


def get_frame(cap):
    ret, frame = cap.read()
    # check if frame is read
    if not ret:
        print("Failed to grab frame")
        return None
    
    return frame 

# display the frame in a window
def show_frame(window_name, frame): 
    cv2.imshow(window_name, frame)
    
# close the window when q is pressed
def cleanup(cap):
    cap.release()
    cv2.destroyAllWindows()
    
