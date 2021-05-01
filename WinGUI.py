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
        # Fill the background with white
        self.screen.fill(self.backCol)
        #pygame.mouse.set_visible(False)
        clock = pygame.time.Clock()

    def drawFrameMenu(self, mouseCoords, button1Fac, button2Fac):
        pygame.mouse.set_visible(False)
        self.screen.fill(self.backCol)
        pygame.draw.rect(self.screen, (179, 120, 43), pygame.Rect(c.windowDims[0]*0.6, c.windowDims[1]*0.1, c.windowDims[0] *0.37, c.windowDims[1]*0.8))
        pygame.draw.rect(self.screen, (255, 163, 43), pygame.Rect(c.windowDims[0]*0.6, c.windowDims[1]*0.1, c.windowDims[0] *0.37, c.windowDims[1]*0.8* button1Fac))
        pygame.draw.rect(self.screen, (179, 43, 43), pygame.Rect(c.windowDims[0]*0.05, c.windowDims[1]*0.05, c.windowDims[0]*0.3, c.windowDims[1]*0.25))
        pygame.draw.rect(self.screen, (237, 14, 14), pygame.Rect(c.windowDims[0]*0.05, c.windowDims[1]*0.05, c.windowDims[0]*0.3, c.windowDims[1]*0.25 * button2Fac))

        font = pygame.font.SysFont(None, int(c.windowDims[0]*0.2))
        img = font.render("Play", True, self.backCol)
        center = img.get_rect(center=(c.windowDims[0]*0.78, c.windowDims[1] * 0.5))
        self.screen.blit(img, center)

        font = pygame.font.SysFont(None, int(c.windowDims[0]*0.17))
        img = font.render("Exit", True, self.backCol)
        center = img.get_rect(center=(c.windowDims[0] * 0.195, c.windowDims[1] * 0.175))
        self.screen.blit(img, center)

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
            self.drawFrameGameover([c.halfDims, c.halfDims], 0, 0, False)
            co.drawRect(self.screen, (self.backCol[0], self.backCol[1], self.backCol[2], 255 * (1 - (i / 49))), pygame.Rect(0, 0, c.windowDims[0], c.windowDims[1]))
            pygame.display.flip()
            pygame.display.update()
            t.sleep(0.005)


    def drawFrameGameover(self, mouseCoords, button1Fac, button2Fac, update):
        self.screen.fill(self.backCol)
        pygame.draw.rect(self.screen, (179, 120, 43), pygame.Rect(c.windowDims[0]*0.55, c.windowDims[1]*0.05, c.windowDims[0]*0.4, c.windowDims[1]*0.4))
        pygame.draw.rect(self.screen, (255, 163, 43), pygame.Rect(c.windowDims[0]*0.55, c.windowDims[1]*0.05, c.windowDims[0]*0.4, c.windowDims[1]*0.4 * button1Fac))
        pygame.draw.rect(self.screen, (179, 43, 43), pygame.Rect(c.windowDims[0]*0.05, c.windowDims[1]*0.05, c.windowDims[0]*0.4, c.windowDims[1]*0.4))
        pygame.draw.rect(self.screen, (237, 14, 14), pygame.Rect(c.windowDims[0]*0.05, c.windowDims[1]*0.05, c.windowDims[0]*0.4, c.windowDims[1]*0.4 * button2Fac))

        font = pygame.font.SysFont(None, int(c.windowDims[0]*0.15))
        img = font.render("Retry", True, self.backCol)
        center = img.get_rect(center=(c.windowDims[0]*0.75, c.windowDims[1] * 0.275))
        self.screen.blit(img, center)

        font = pygame.font.SysFont(None, int(c.windowDims[0]*0.15))
        img = font.render("Exit", True, self.backCol)
        center = img.get_rect(center=(c.windowDims[0] * 0.25, c.windowDims[1] * 0.275))
        self.screen.blit(img, center)

        font = pygame.font.SysFont(None, int(c.windowDims[0]*0.2))
        img = font.render('Game Over', True, (255, 255, 255))
        center = img.get_rect(center=(c.halfDims[0], c.windowDims[1]*0.7))
        self.screen.blit(img, center)

        for i in range(len(mouseCoords)):
            co.drawCircle(self.screen, (255, 255, 255, 255 * (i / (len(mouseCoords) - 1))), mouseCoords[i], 50, 5)

        if update:
            pygame.display.flip()
            pygame.display.update()

    def activateGame(self, menu1):
        if menu1:
            for i in range(5):
                self.screen.fill(self.backCol)
                pygame.draw.rect(self.screen, (207, 154, 85), pygame.Rect(c.windowDims[0]*0.6, c.windowDims[1]*0.1, c.windowDims[0] *0.37, c.windowDims[1]*0.8))
                font = pygame.font.SysFont(None, int(c.windowDims[0] * 0.2))
                img = font.render("Play", True, self.backCol)
                center = img.get_rect(center=(c.windowDims[0] * 0.78, c.windowDims[1] * 0.5))
                self.screen.blit(img, center)
                pygame.display.flip()
                pygame.display.update()
                t.sleep(0.05)
                pygame.draw.rect(self.screen, (179, 120, 43), pygame.Rect(c.windowDims[0]*0.6, c.windowDims[1]*0.1, c.windowDims[0] *0.37, c.windowDims[1]*0.8))
                font = pygame.font.SysFont(None, int(c.windowDims[0] * 0.2))
                img = font.render("Play", True, self.backCol)
                center = img.get_rect(center=(c.windowDims[0] * 0.78, c.windowDims[1] * 0.5))
                self.screen.blit(img, center)
                pygame.display.flip()
                pygame.display.update()
                t.sleep(0.05)
        else:
            for i in range(5):
                self.screen.fill(self.backCol)
                pygame.draw.rect(self.screen, (207, 154, 85), pygame.Rect(c.windowDims[0]*0.55, c.windowDims[1]*0.05, c.windowDims[0]*0.4, c.windowDims[1]*0.4))
                font = pygame.font.SysFont(None, int(c.windowDims[0]*0.15))
                img = font.render("Retry", True, self.backCol)
                center = img.get_rect(center=(c.windowDims[0] * 0.75, c.windowDims[1] * 0.275))
                self.screen.blit(img, center)
                pygame.display.flip()
                pygame.display.update()
                t.sleep(0.05)
                pygame.draw.rect(self.screen, (179, 120, 43), pygame.Rect(c.windowDims[0]*0.55, c.windowDims[1]*0.05, c.windowDims[0]*0.4, c.windowDims[1]*0.4))
                font = pygame.font.SysFont(None, int(c.windowDims[0]*0.15))
                img = font.render("Retry", True, self.backCol)
                center = img.get_rect(center=(c.windowDims[0] * 0.75, c.windowDims[1] * 0.275))
                self.screen.blit(img, center)
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

        font = pygame.font.SysFont(None, int(c.windowDims[0]*0.07))
        img = font.render('Score: ' + str(c.score), True, co((20, 255, 130)).interpColors((255, 255, 255), self.ball.bounds[1].backVal))
        center = img.get_rect(center=(c.windowDims[0]*0.1, c.windowDims[1]*0.4))
        self.screen.blit(img, center)

        font = pygame.font.SysFont(None, int(c.windowDims[0]*0.07))
        img = font.render('Lives: ' + str(self.ball.lives), True, co((255, 0, 0)).interpColors((255, 255, 255), self.ball.bounds[0].frontVal))
        center = img.get_rect(center=(c.windowDims[0] * 0.1, c.windowDims[1] * 0.6))
        self.screen.blit(img, center)

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
