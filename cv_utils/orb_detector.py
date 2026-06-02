import cv2


class ORBDetector: 
    
    def __init__(self, template_path):
        
        self.orb = cv2.ORB_create()
        
        template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
        
        self.kp1, self.des1 = (self.orb.detectAndCompute(template, None))
        
        self.matcher = cv2.BFMatcher(
            cv2.NORM_HAMMING, 
            crossCheck=True
        )
        
    def detect(self, frame):
            
            gray = cv2.cvtColor(
                frame, 
                cv2.COLOR_BGR2GRAY
            )
            
            kp2, des2 = self.orb.detectAndCompute(gray, None)
            
            if des2 is None:
                return frame

            matches = self.matcher.match(self.des1, des2)
            
            matches = sorted(matches, key=lambda x: x.distance)
            
            print(len(matches))
            
            cv2.putText(
                
                frame,
                f"Matches: {len(matches)}",
                (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (255, 255, 255),
                2
            )
            
            good_matches = [
                m for m in matches if m.distance < 40
            ]
            
            
            if len(good_matches) > 15: 
                
                cv2.putText(
                    frame, 
                    "CELCIUS DETECTED", 
                    (50, 50), 
                    cv2.FONT_HERSHEY_SIMPLEX, 
                    1, 
                    (0, 255, 0), 
                    2
                )
                
                
            return frame