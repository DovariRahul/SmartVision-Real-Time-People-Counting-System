import cv2

def draw_boxes(frame, tracks):
    for track in tracks:
        x1, y1, x2, y2, track_id = track
        cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (255,0,0), 2)
        cv2.putText(frame, f"ID {int(track_id)}",
                    (int(x1), int(y1)-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255), 2)

def draw_line(frame, y):
    cv2.line(frame, (0, y), (frame.shape[1], y), (0,255,255), 2)

def draw_count(frame, count):
    cv2.putText(frame, f"Count: {count}",
                (20,40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
