import cv2
import yaml

from src.video.video_stream import VideoStream
from src.background.bg_subtractor import BackgroundSubtractor
from src.detection.yolo_detector import YOLODetector
from src.tracking.sort_tracker import SortTracker
from src.counting.occupancy_counter import OccupancyCounter
from src.utils.visualization import draw_boxes, draw_line, draw_count
from src.utils.fps import FPS

def run():
    with open("config/config.yaml") as f:
        cfg = yaml.safe_load(f)

    video = VideoStream(
        cfg["video"]["source"],
        cfg["video"]["width"],
        cfg["video"]["height"]
    )

    detector = YOLODetector(
        cfg["detection"]["model_path"],
        cfg["detection"]["confidence"],
        cfg["detection"]["classes"]
    )

    tracker = SortTracker(
        cfg["tracking"]["max_age"],
        cfg["tracking"]["min_hits"],
        cfg["tracking"]["iou_threshold"]
    )

    counter = OccupancyCounter()
    fps = FPS()
    window_name = "People Counter"
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)


    while True:
        ret, frame = video.read()
        if not ret:
            break

        detections = detector.detect(frame)
        tracks = tracker.update(detections)
        count = counter.update(tracks)

        draw_boxes(frame, tracks)
        draw_count(frame, count)

        cv2.putText(frame, f"FPS: {fps.calculate()}",
                    (500,40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)

        cv2.imshow(window_name, frame)


        if cv2.waitKey(1) & 0xFF == 27:
            break

    video.release()
    cv2.destroyAllWindows()
