import pyautogui

#Change DEBUG to toggle verbosity and reduced performance
DEBUG = False

#Change to toggle game with or without camera
hasCamera = False

gravity = -9.8
timeMultiplier = 1
windowDims = pyautogui.size()
halfDims = [windowDims[0]/2, windowDims[1]/2]
score = 0