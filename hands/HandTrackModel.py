import cv2
import mediapipe as mp
import settings as c


class Track:
    def __init__(self, fw, fh):
        self.mpHands = mp.solutions.hands
        self.mpDraw = mp.solutions.drawing_utils
        self.hands = self.mpHands.Hands(max_num_hands=1,
                                        min_tracking_confidence=0.5,
                                        min_detection_confidence=0.5)
        self.w = fw
        self.h = fh
        self.pos = c.windowDims
        self.points_length = 2
        self.last_points = [c.halfDims]*self.points_length

    def get_interpolated_hand_pos(self):
        x = 0
        y = 0
        for point in self.last_points:
            x += point[0]
            y += point[1]
        return x/self.points_length, y/self.points_length

    # Gets hand positions
    def create_hand_position(self, frame):
        point = 0
        coordList = []

        frame = cv2.flip(frame, 1)
        RGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = self.hands.process(RGB)

        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                cx = handLms.landmark[9].x
                cy = handLms.landmark[9].y
                self.last_points.pop(0)
                self.last_points.append([cx, cy])
                if c.DEBUG:
                    self.mpDraw.draw_landmarks(frame, handLms, self.mpHands.HAND_CONNECTIONS)

        return frame
