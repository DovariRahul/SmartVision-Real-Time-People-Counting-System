import cv2

class BackgroundSubtractor:
    def __init__(self):
        self.bg = cv2.createBackgroundSubtractorMOG2(
            history=500, varThreshold=50, detectShadows=True
        )

    def apply(self, frame):
        return self.bg.apply(frame)
