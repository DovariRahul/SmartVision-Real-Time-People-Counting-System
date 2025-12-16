from ultralytics import YOLO

class YOLODetector:
    def __init__(self, model_path, confidence, classes):
        self.model = YOLO(model_path)
        self.conf = confidence
        self.classes = classes

    def detect(self, frame):
        results = self.model(frame, conf=self.conf, classes=self.classes, verbose=False)
        detections = []

        for r in results:
            for box in r.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                detections.append([x1, y1, x2, y2])

        return detections
