import cv2
import numpy as np


class TemplateDetector:
    
    def __init__(self, template_path): 
        
        self.template = cv2.imread(
            template_path, 
            cv2.IMREAD_GRAYSCALE
        )
        
        def detect(self, frame):
            
            gray = cv2.cvtColor(
                frame, 
                cv2.COLOR_BGR2GRAY
            )
            
        result = cv2.matchTemplate(
            gray, 
            self.template, 
            cv2.TM_CCOEFF_NORMED
        )
        
        threshold = 0.8
        
        loc = np.where(result >= threshold)
        
        for pt in zip(*loc[::-1]):
            cv2.rectangle(
                frame, 
                pt, 
                (
                    pt[0] + self.template.shape[1], 
                    pt[1] + self.template.shape[0]
                ),
                (0, 255, 0,),
                 2
            
            )
            
            cv2.putText(
                frame, 
                "Caffeine Detected", 
                (pt[0], pt[1] - 10), 
                cv2.FONT_HERSHEY_SIMPLEX, 
                0.7, 
                (0, 255, 0), 
                2
            )
            
            return frame 