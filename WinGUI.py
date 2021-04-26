import time as t
import pygame
from Physics import Ball as b
import settings as c
from Physics.ColorMath import Color as co
import pyautogui


class DrawableWin:
    # Declare Width and Height of window
    width, height = pyautogui.size()
    #background color
    backCol = [16, 16, 16]
    ballCol = [200, 200, 200]

    ball = b.Ball
    screen = pygame.display.set_mode([width, height])

    def __init__(self, ball):
        self.ball = ball
        pygame.init()
        self.screen = pygame.display.set_mode([self.width, self.height])
        running = True
        # Fill the background with white
        self.screen.fill(self.backCol)
        #pygame.mouse.set_visible(False)
        clock = pygame.time.Clock()

    def drawFrameMenu(self, mouseCoords, button1Fac, button2Fac):
        pygame.mouse.set_visible(False)
        self.screen.fill(self.backCol)
        pygame.draw.rect(self.screen, (179, 120, 43), pygame.Rect(c.halfDims[0] + 50, 50, c.halfDims[0] - 100, c.windowDims[1] - 100))
        pygame.draw.rect(self.screen, (255, 163, 43), pygame.Rect(c.halfDims[0] + 50, 50, c.halfDims[0] - 100, (c.windowDims[1] - 100) * button1Fac))
        pygame.draw.rect(self.screen, (179, 43, 43), pygame.Rect(50, 50, 400, 200))
        pygame.draw.rect(self.screen, (237, 14, 14), pygame.Rect(50, 50, 400, 200 * button2Fac))

        font = pygame.font.SysFont(None, 300)
        img = font.render("Play", True, self.backCol)
        self.screen.blit(img, (c.halfDims[0] + 250, c.halfDims[1] - 100))

        font = pygame.font.SysFont(None, 200)
        img = font.render("Exit", True, self.backCol)
        self.screen.blit(img, (100, 90))

        for i in range(len(mouseCoords)):
            co.drawCircle(self.screen, (255, 255, 255, 255 * (i / (len(mouseCoords) - 1))), mouseCoords[i], 50, 5)
        pygame.display.flip()
        pygame.display.update()

    def activateGameOver(self):
        for i in range(50):
            self.drawFrameGame(False)
            co.drawRect(self.screen, (self.backCol[0], self.backCol[1], self.backCol[2], 255 * (i / 49)), pygame.Rect(0, 0, c.windowDims[0], c.windowDims[1]))
            self.ball.drawRed(self.screen)
            pygame.display.flip()
            pygame.display.update()
            t.sleep(0.005)

        for i in range(50):
            self.drawFrameGameover([(0, 0), (0, 0)], 0, 0, False)
            co.drawRect(self.screen, (self.backCol[0], self.backCol[1], self.backCol[2], 255 * (1 - (i / 49))), pygame.Rect(0, 0, c.windowDims[0], c.windowDims[1]))
            pygame.display.flip()
            pygame.display.update()
            t.sleep(0.005)


    def drawFrameGameover(self, mouseCoords, button1Fac, button2Fac, update):
        pygame.mouse.set_visible(False)
        self.screen.fill(self.backCol)
        pygame.draw.rect(self.screen, (179, 120, 43), pygame.Rect(c.halfDims[0] + 50, 50, c.halfDims[0] - 100, c.halfDims[1] - 100))
        pygame.draw.rect(self.screen, (255, 163, 43), pygame.Rect(c.halfDims[0] + 50, 50, c.halfDims[0] - 100, (c.halfDims[1] - 100) * button1Fac))
        pygame.draw.rect(self.screen, (179, 43, 43), pygame.Rect(50, 50, c.halfDims[0] - 100, c.halfDims[1] - 100))
        pygame.draw.rect(self.screen, (237, 14, 14), pygame.Rect(50, 50, c.halfDims[0] - 100, (c.halfDims[1] - 100) * button2Fac))

        font = pygame.font.SysFont(None, 200)
        img = font.render("Retry", True, self.backCol)
        self.screen.blit(img, (c.halfDims[0] + 290, c.halfDims[1] - 330))

        font = pygame.font.SysFont(None, 200)
        img = font.render("Exit", True, self.backCol)
        self.screen.blit(img, (330, c.halfDims[1] - 330))

        font = pygame.font.SysFont(None, 350)
        img = font.render('Game Over', True, (255, 255, 255))
        self.screen.blit(img, (50, c.windowDims[1] - 540))

        for i in range(len(mouseCoords)):
            co.drawCircle(self.screen, (255, 255, 255, 255 * (i / (len(mouseCoords) - 1))), mouseCoords[i], 50, 5)

        if update:
            pygame.display.flip()
            pygame.display.update()

    def activateGame(self, menu1):
        if menu1:
            for i in range(5):
                self.screen.fill(self.backCol)
                pygame.draw.rect(self.screen, (207, 154, 85), pygame.Rect(c.halfDims[0] + 50, 50, c.halfDims[0] - 100, c.windowDims[1] - 100))
                pygame.display.flip()
                pygame.display.update()
                t.sleep(0.05)
                pygame.draw.rect(self.screen, (179, 120, 43), pygame.Rect(c.halfDims[0] + 50, 50, c.halfDims[0] - 100, c.windowDims[1] - 100))
                pygame.display.flip()
                pygame.display.update()
                t.sleep(0.05)
        else:
            for i in range(5):
                self.screen.fill(self.backCol)
                pygame.draw.rect(self.screen, (207, 154, 85), pygame.Rect(c.halfDims[0] + 50, 50, c.halfDims[0] - 100, c.halfDims[1] - 100))
                font = pygame.font.SysFont(None, 200)
                img = font.render("Retry", True, self.backCol)
                self.screen.blit(img, (c.halfDims[0] + 290, c.halfDims[1] - 330))
                pygame.display.flip()
                pygame.display.update()
                t.sleep(0.05)
                pygame.draw.rect(self.screen, (179, 120, 43), pygame.Rect(c.halfDims[0] + 50, 50, c.halfDims[0] - 100, c.halfDims[1] - 100))
                font = pygame.font.SysFont(None, 200)
                img = font.render("Retry", True, self.backCol)
                self.screen.blit(img, (c.halfDims[0] + 290, c.halfDims[1] - 330))
                pygame.display.flip()
                pygame.display.update()
                t.sleep(0.05)

        for i in range(50):
            self.drawFrameGame(False)
            co.drawRect(self.screen, (self.backCol[0], self.backCol[1], self.backCol[2], 255 * (1 - (i / 49))), pygame.Rect(0, 0, c.windowDims[0], c.windowDims[1]))
            pygame.display.flip()
            pygame.display.update()
            t.sleep(0.005)

        for i in range(3):
            self.drawFrameGame(False)
            font = pygame.font.SysFont(None, 500)
            img = font.render(str(3-i), True, (255, 255, 255))
            self.screen.blit(img, (c.halfDims[0] - 100, c.halfDims[1] - 150))
            pygame.display.flip()
            pygame.display.update()
            t.sleep(0.7)
        self.drawFrameGame(False)
        font = pygame.font.SysFont(None, 500)
        img = font.render("GO!", True, (255, 255, 255))
        self.screen.blit(img, (c.halfDims[0] - 330, c.halfDims[1] - 150))
        pygame.display.flip()
        pygame.display.update()
        t.sleep(0.7)
        return True


    def drawFrameGame(self, update):
        self.screen.fill(self.backCol)
        font = pygame.font.SysFont(None, 70)
        img = font.render('Score: ' + str(c.score), True, co((20, 255, 130)).interpColors((255, 255, 255), self.ball.bounds[1].backVal))
        self.screen.blit(img, (30, c.halfDims[1] + 25))

        font = pygame.font.SysFont(None, 70)
        img = font.render('Lives: ' + str(self.ball.lives), True, co((255, 0, 0)).interpColors((255, 255, 255), self.ball.bounds[0].frontVal))
        self.screen.blit(img, (30, c.halfDims[1] - 25))

        # Draw arena first
        self.ball.bounds[0].drawFillBack(self.screen, (100, 100, 100, 100), (100, 100, 100, 20))
        self.ball.bounds[0].drawFillRight(self.screen, (100, 100, 100, 100), (100, 100, 100, 20))
        self.ball.bounds[0].drawFillLeft(self.screen, (100, 100, 100, 100), (100, 100, 100, 20))
        self.ball.bounds[0].drawFillTop(self.screen, (100, 100, 100, 100), (100, 100, 100, 20))
        self.ball.bounds[0].drawFillBottom(self.screen, (100, 100, 100, 100), (100, 100, 100, 20))
        self.ball.bounds[0].drawFillFront(self.screen, (255, 0, 0, 255), (100, 100, 100, 20))
        self.ball.bounds[0].drawWire(self.screen, 2)

        # Draw opponent second
        self.ball.bounds[2].drawFillBack(self.screen, (100, 100, 100, 100), (150, 100, 100, 20))
        self.ball.bounds[2].drawFillRight(self.screen, (100, 100, 100, 100), (150, 100, 100, 20))
        self.ball.bounds[2].drawFillLeft(self.screen, (100, 100, 100, 100), (150, 100, 100, 20))
        self.ball.bounds[2].drawFillTop(self.screen, (100, 100, 100, 100), (150, 100, 100, 20))
        self.ball.bounds[2].drawFillBottom(self.screen, (100, 100, 100, 100), (150, 100, 100, 20))
        self.ball.bounds[2].drawFillFront(self.screen, (255, 0, 0, 255), (150, 100, 100, 20))
        self.ball.bounds[2].drawWire(self.screen, 2)

        #Draw Power ups
        if len(self.ball.bounds) == 4:
            self.ball.bounds[3].drawFillBack(self.screen, (100, 100, 255, 100), (100, 100, 255, 20))
            self.ball.bounds[3].drawFillRight(self.screen, (100, 100, 255, 100), (100, 100, 255, 20))
            self.ball.bounds[3].drawFillLeft(self.screen, (100, 100, 255, 100), (100, 100, 255, 20))
            self.ball.bounds[3].drawFillTop(self.screen, (100, 100, 255, 100), (100, 100, 255, 20))
            self.ball.bounds[3].drawFillBottom(self.screen, (100, 100, 255, 100), (100, 100, 255, 20))
            self.ball.bounds[3].drawFillFront(self.screen, (100, 100, 255, 255), (100, 100, 255, 20))
            self.ball.bounds[3].drawWire(self.screen, 2)

        # Draw player on top
        self.ball.bounds[1].drawFillBack(self.screen, (100, 255, 130, 255), (100, 100, 100, 20))
        self.ball.bounds[1].drawFillRight(self.screen, (100, 100, 100, 100), (100, 100, 100, 20))
        self.ball.bounds[1].drawFillLeft(self.screen, (100, 100, 100, 100), (100, 100, 100, 20))
        self.ball.bounds[1].drawFillTop(self.screen, (100, 100, 100, 100), (100, 100, 100, 20))
        self.ball.bounds[1].drawFillBottom(self.screen, (100, 100, 100, 100), (100, 100, 100, 20))
        self.ball.bounds[1].drawFillFront(self.screen, (100, 100, 100, 100), (100, 100, 100, 20))
        self.ball.bounds[1].drawWire(self.screen, 2)

        self.ball.draw(self.screen)

        if update:
            pygame.display.flip()
            pygame.display.update()
