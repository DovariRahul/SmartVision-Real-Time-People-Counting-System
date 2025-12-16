class OccupancyCounter:
    def __init__(self, max_missing_frames=30):
        self.active_ids = {}
        self.max_missing = max_missing_frames

    def update(self, tracks):
        current_ids = set()

        for track in tracks:
            track_id = int(track[4])
            current_ids.add(track_id)

            if track_id not in self.active_ids:
                self.active_ids[track_id] = 0
            else:
                self.active_ids[track_id] = 0

        # Remove disappeared IDs
        for track_id in list(self.active_ids.keys()):
            if track_id not in current_ids:
                self.active_ids[track_id] += 1
                if self.active_ids[track_id] > self.max_missing:
                    del self.active_ids[track_id]

        return len(self.active_ids)
