import pyautogui

#Change DEBUG to toggle verbosity and reduced performance
DEBUG = False

#Change to toggle game with or without camera
hasCamera = True

#Draw Wire only
drawWireOnly = False

#Draw Mesh only
drawMeshOnly = True

gravity = -9.8
timeMultiplier = 1
windowDims = pyautogui.size()
#windowDims = [1080, 720]
defaultDims = [1920, 1080]
halfDims = [windowDims[0]/2, windowDims[1]/2]
resScale = min(windowDims) / min(defaultDims)
score = 0