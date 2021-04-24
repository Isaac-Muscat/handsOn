import cv2
import mediapipe as mp
from mediapipe import solutions
import numpy as np
import os
import ctypes
import time
import pyautogui as mouse

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
def get_hand_position(frame):
    frame = cv2.flip(frame, 1)
    camRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    hand_list = []
    results = hands.process(camRGB)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            hand_list.append(handLms.landmark)


    return hand_list