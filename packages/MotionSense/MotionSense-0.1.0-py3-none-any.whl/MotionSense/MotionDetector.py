import cv2
import numpy as np


class MotionDetector:

    def __init__(self):
        self.previous_frame = None
        self.current_frame = None

    def motion_detector(self, next_frame):
        result = []
        next_frame = cv2.cvtColor(next_frame, cv2.COLOR_BGR2GRAY)
        next_frame = cv2.GaussianBlur(src=next_frame, ksize=(5, 5), sigmaX=0)
        if self.previous_frame is None:
            self.previous_frame = next_frame
            return
        if self.current_frame is None:
            self.current_frame = next_frame
        else:
            self.previous_frame = self.current_frame
            self.current_frame = next_frame

        prepared_frame = next_frame.copy()
        previous_frame = self.previous_frame.copy()
        # 1. Load image; convert to RGB
        # cv2.imshow("dre", self.previous_frame)

        # 2. Prepare image; grayscale and blur

        # calculate difference and update previous frame
        diff_frame = cv2.absdiff(src1=previous_frame, src2=prepared_frame)
        # previous_frame = prepared_frame

        # 4. Dilute the image a bit to make differences more seeable; more suitable for contour detection
        kernel = np.ones((5, 5))
        diff_frame = cv2.dilate(diff_frame, kernel, 1)

        # 5. Only take different areas that are different enough (>20 / 255)
        thresh_frame = cv2.threshold(src=diff_frame, thresh=50, maxval=255, type=cv2.THRESH_BINARY)[1]

        id = 0
        contours, _ = cv2.findContours(image=thresh_frame, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            if cv2.contourArea(contour) < 50:
                # too small: skip!
                continue
            (x, y, w, h) = cv2.boundingRect(contour)
            bbox = {'id': id,
                    'x': x / next_frame.shape[1],
                    'y': y / next_frame.shape[0],
                    'w': w / next_frame.shape[1],
                    'h': h / next_frame.shape[0],
                    'label': "Motion",
                    'acc': -1
                    }
            result.append(bbox)
            id += 1
        return result
