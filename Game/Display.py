#-------------------------------------------------
"Importieren Packages"
import pygame
import os
import sys
import random
pygame.init()
#-------------------------------------------------
"Screen erstellen"
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
#screen = pygame.display.set_mode((1920, 1180), pygame.RESIZABLE)
pygame.display.set_caption("Dodge Dungeon", "Dodge Dungeon")
#-------------------------------------------------
"Importieren von Grafiken"
import Gi as gi
#-------------------------------------------------
"Raum erstellen"
class Room():
    def __init__(self, size):
        self.size = size
        counter = self.size
        randomlist = [0]*counter*counter
        for ph in range(counter*counter):
                randomlist[ph] = random.randrange(0, 7)

        self.randomlist = randomlist

    def room_blitting(self):
        size = self.size*80
        size2 = size
        sizeholder = size
        counter = int(size/80)
        randomcounter = 0
        randomlist = self.randomlist
        #Boden
        for ph in range(counter):
            for ph in range(counter):
                screen.blit(gi.floorlist[randomlist[randomcounter]], (860 - counter*40 + size, 540 + counter*40 - size2))
                size = size - 80
                randomcounter = randomcounter + 1
            size = sizeholder
            size2 = size2 - 80

        #Wand Oben/Unten
        screen.blit(gi.walllist[0], (860 - counter*40 + 80, 540 - counter*40 - 100))
        for ph in range(counter - 2):
            screen.blit(gi.walllist[1], (860 - counter*40 + size - 80, 540 - counter*40 - 100))
            size = size - 80
        screen.blit(gi.walllist[2], (860 + counter*40, 540 - counter*40 - 100))

        size = sizeholder
        for ph in range(counter):
            screen.blit(gi.walllist[1], (860 - counter * 40 + size, 540 + counter * 40))
            size = size - 80

        #Wand Rechts/Links
        size = sizeholder
        screen.blit(gi.wally1list[0], (860 - counter*40 + 52, 540 - counter*40 - 100))
        screen.blit(gi.wally1list[0], (860 + counter*40 + 72, 540 - counter*40 - 100))
        for ph in range(counter):
            screen.blit(gi.wally2list[0], (860 - counter*40 + 52, 540 + counter*40 - size))
            screen.blit(gi.wally2list[0], (860 + counter*40 + 72, 540 + counter*40 - size))
            size = size - 80
        screen.blit(gi.wally1list[1], (860 - counter * 40 + 52, 540 + counter * 40))
        screen.blit(gi.wally1list[2], (860 + counter * 40 + 72, 540 + counter * 40))
#-------------------------------------------------