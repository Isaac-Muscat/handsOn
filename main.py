import random
from Physics import Math as M
from Physics import Ball as B
import time
import WinGUI
import pygame
import settings as c
import hands.HandTrackModel as HandTrackModel
import cv2

#Startup variables and actions
pygame.init()
running = True
average = (0,0)
paddleX, paddleY = average
prevPaddleX, prevPaddleY = average
myHands = None
frame_state = 'menu'
button1Fac = 0
button2Fac = 0
mouseCoords = c.halfDims

# points stored in memory for averaging position of game cursor
pointLength = 6
lastPoints = [(0, 0)] * pointLength

# set up webcam video capture device
if c.hasCamera:
    cap = cv2.VideoCapture(0)
    if not cap.read():
        cap = cv2.VideoCapture(1)
else:
    hasCamera = False

# calculate the average of the last points
def averageOfLast(points):
    vx = 0
    vy = 0
    for v in range(len(points) - 1):
        vx = points[v][0] + vx
        vy = points[v][1] + vy
    average = (int(vx / (len(points) - 1)), int(vy / (len(points) - 1)))
    return average


def setPoints(coordList):
    # remove the last point in the list and add the new one
    if coordList:
        lastPoints.pop(0)
        lastPoints.append(coordList[0])

    # get the average of the points
    average = averageOfLast(lastPoints)

    posX = c.windowDims[0] * (average[0] / myHands.w) / 2
    posY = c.windowDims[1] * (average[1] / myHands.h) / 2

    return posX, posY

#Setup game objects and initialize the window
bounds = []
walls = M.BoundRect(M.Vector3(-500, -500, 0), M.Vector3(500, 500, 1000), M.Vector3(0, 0, 0), True)
player_paddle = M.BoundRect(M.Vector3(-200, -200, 0), M.Vector3(200, 200, 100), M.Vector3(0, 0, 50), False)
ai_paddle = M.BoundRect(M.Vector3(-50, -50, 970), M.Vector3(50, 50, 1000), M.Vector3(0, 0, 985), False)
bounds.append(walls)
bounds.append(player_paddle)
bounds.append(ai_paddle)
ball = B.Ball(50, M.Vector3(0, 0, 500), M.Vector3(1000, 100, 1000), bounds)
w = WinGUI.DrawableWin(ball)
lastTime = time.time()

#Main Loop
while running:
    # Calculate delta time in seconds
    currentTime = time.time()
    deltaTime = (currentTime - lastTime)
    lastTime = currentTime

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    if c.hasCamera:
        ret, frame = cap.read()

        # setup hands model if it does not exist
        if myHands is None:
            myHands = HandTrackModel.Track(len(frame[0]), len(frame))

        # pass the frame and list of points for tracking
        frame= myHands.create_hand_position(frame)
        pos = myHands.get_interpolated_hand_pos()
        posX = c.windowDims[0] * pos[0]
        posY = c.windowDims[1] * pos[1]
        mouseCoords = (posX, posY)

        # display the resulting frame
        if c.DEBUG:
            cv2.imshow('frame', frame)

    if not c.hasCamera:
        mouseCoords = pygame.mouse.get_pos()

    paddleX, paddleY = mouseCoords
    lastPoints.pop(0)
    lastPoints.append(mouseCoords)

    deltaBlock = M.Vector3(paddleX - c.halfDims[0], c.windowDims[1] - paddleY - c.halfDims[1], 50)
    ball.bounds[1].moveBlock(deltaBlock)

    #Uncomment for ai
    # ball.bounds[2].moveBlock(M.Vector3(ball.pos.x, ball.pos.y, 0))

    if frame_state == 'game':
        ball.PhysicsTick(deltaTime)
        w.drawFrameGame(True)
        if ball.lives <= 0:
            w.activateGameOver()
            frame_state = 'gameover'
            c.score = 0
            ball.lives = 3
            ball.pos = M.Vector3(0, 0, 500)
            ball.velocity = M.Vector3(random.randint(-1000, 1000), random.randint(-1000, 1000), 1000)
    elif frame_state == 'menu':
        # c.halfDims[0] + 50, 50, c.halfDims[0] - 100, c.windowDims[1] - 100
        if c.halfDims[0] + 50 < paddleX < c.windowDims[0] - 50 and 50 < paddleY < c.windowDims[1] - 50:
            button1Fac += 0.007
            if button1Fac > 1:
                button1Fac = 1
                if w.activateGame(True):
                    lastTime = time.time()
                    frame_state = 'game'
        else:
            button1Fac -= 0.01
            if button1Fac < 0:
                button1Fac = 0

        if 50 < paddleX < 450 and 50 < paddleY < 250:
            button2Fac += 0.007
            if button2Fac > 1:
                button2Fac = 1
        else:
            button2Fac -= 0.01
            if button2Fac < 0:
                button2Fac = 0

        w.drawFrameMenu(lastPoints, button1Fac, button2Fac)
    elif frame_state == 'gameover':
        # c.halfDims[0] + 50, 50, c.halfDims[0] - 100, c.halfDims[1] - 100
        if c.halfDims[0] + 50 < paddleX < c.windowDims[0] - 50 and 50 < paddleY < c.halfDims[1] - 50:
            button1Fac += 0.007
            if button1Fac > 1:
                button1Fac = 1
                if w.activateGame(False):
                    lastTime = time.time()
                    frame_state = 'game'
        else:
            button1Fac -= 0.01
            if button1Fac < 0:
                button1Fac = 0

        # 50, 50, c.halfDims[0] - 100, c.halfDims[1] - 100
        if 50 < paddleX < c.halfDims[0] - 50 and 50 < paddleY < c.halfDims[1] - 50:
            button2Fac += 0.007
            if button2Fac > 1:
                button2Fac = 1
                break
        else:
            button2Fac -= 0.01
            if button2Fac < 0:
                button2Fac = 0
        w.drawFrameGameover(lastPoints, button1Fac, button2Fac, True)

if c.hasCamera:
    cap.release()
    cv2.destroyAllWindows()
pygame.quit()