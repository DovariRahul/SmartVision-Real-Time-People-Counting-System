import numpy as np
from .sort import Sort


class SortTracker:
    def __init__(self, max_age, min_hits, iou_threshold):
        self.tracker = Sort(
            max_age=max_age,
            min_hits=min_hits,
            iou_threshold=iou_threshold
        )

    def update(self, detections):
        if len(detections) == 0:
            return np.empty((0, 5))
        dets = np.array(detections)
        return self.tracker.update(dets)
