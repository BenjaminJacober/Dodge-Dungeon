#-------------------------------------------------
"Importieren Packages"
import pygame
import os
import sys
import random
pygame.init()
#-------------------------------------------------
"Importieren von Display"
import Display as ds
#-------------------------------------------------
"Einen Raum erstellen"
room = ds.Room(5)
#-------------------------------------------------
"Player erstellen"
class Player():
    def __init__(self, xPos, yPos, direction):
        self.xPos = xPos
        self.yPos = yPos
        self.direction = direction
        self.state = 0
        self.x1speed = 0
        self.x2speed = 0
        self.y1speed = 0
        self.y2speed = 0
        self.image = 0
        self.timer = 0

    def player_blitting(self):
        direction = self.direction
        if self.image > 6:
            self.image = 6

        if direction == 0:
            ds.screen.blit(ds.gi.playerlist[self.image], (self.xPos, self.yPos))
        else:
            ds.screen.blit(pygame.transform.flip(ds.gi.playerlist[self.image], True, False), (self.xPos, self.yPos))

    def player_movement(self):
        if self.x1speed == 1:
            self.direction = 1
            self.state = 1
            self.xPos = self.xPos - 0.5
        if self.x2speed == 1:
            self.direction = 0
            self.state = 1
            self.xPos = self.xPos + 0.5
        if self.y1speed == 1:
            self.state = 1
            self.yPos = self.yPos + 0.5
        if self.y2speed == 1:
            self.state = 1
            self.yPos = self.yPos - 0.5
        if self.x1speed == 0 and self.x2speed == 0 and self.y1speed == 0 and self.y2speed == 0:
            self.state = 0

    def player_animation(self):
        state = self.state
        if state == 0:
            self.timer = self.timer + 1
            if self.timer >= 130:
                self.image = self.image + 1
                self.timer = 0
            if self.image >= 2:
                self.image = 0

        if state == 1:
            self.timer = self.timer + 1
            if self.timer >= 85:
                self.image = self.image + 1
                self.timer = 0
            if self.image >= 7:
                self.image = 3

    def player_collision(self):
        size = room.size
        xPos = self.xPos
        yPos = self.yPos
        maxrightX = 850 + size*40
        maxleftX = 900 - size*40
        maxupY = 440 + size*40
        maxdownY = 440 - size*40
        if xPos > maxrightX:
            self.xPos = maxrightX
        if xPos < maxleftX:
            self.xPos = maxleftX
        if yPos > maxupY:
            self.yPos = maxupY
        if yPos < maxdownY:
            self.yPos = maxdownY
#-------------------------------------------------
"Einen Player erstellen"
player1 = Player(850 + room.size*40, 440 + room.size*40, 0)
#-------------------------------------------------
"Fallen"
class Trap():
    def __init__(self, TrapNr, xPos, yPos):
        self.TrapNr = TrapNr
        self.xPos = xPos
        self.yPos = yPos
        self.image = 0
        self.state = 0
        self.timer = 0

    def trap_blitting(self):
        xPos = self.xPos
        yPos = self.yPos
        if self.TrapNr == 1:
            ds.screen.blit(ds.gi.spikelist[self.image], (xPos, yPos))

    def trap_collision(self):
        xPos = self.xPos
        yPos = self.yPos
        if player1.xPos > xPos - 80 and player1.xPos < xPos + 20 and player1.yPos > yPos-75 and player1.yPos < yPos-30:
            self.state = 1

    def trap_animation(self):
        if self.state == 1:
            self.timer = self.timer + 1
            if self.timer == 60:
                self.image = self.image + 1
                self.timer = 0
            if self.image > 3:
                player1.xPos = 850 + room.size * 40
                player1.yPos = 440 + room.size * 40
                self.image = 0
                self.state = 0