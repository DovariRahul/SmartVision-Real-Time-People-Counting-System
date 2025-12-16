class LineCounter:
    def __init__(self, line_y):
        self.line_y = line_y
        self.count = 0
        self.counted_ids = set()

    def update(self, tracks):
        for track in tracks:
            x1, y1, x2, y2, track_id = track
            cy = int((y1 + y2) / 2)

            if cy > self.line_y and track_id not in self.counted_ids:
                self.count += 1
                self.counted_ids.add(track_id)

        return self.count
