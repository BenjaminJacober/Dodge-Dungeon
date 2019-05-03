#-------------------------------------------------
"Importieren von Packages"
import pygame
import os
import sys
pygame.init()
#-------------------------------------------------
"Key-Input abfragen"
def keyinput(player):
    pygame.event.pump()
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and keys[pygame.K_s] == True:
        player.x1speed = 1
        player.y1speed = 1
    if keys[pygame.K_a] and keys[pygame.K_w] == True:
        player.x1speed = 1
        player.y2speed = 1
    if keys[pygame.K_d] and keys[pygame.K_s] == True:
        player.x2speed = 1
        player.y1speed = 1
    if keys[pygame.K_d] and keys[pygame.K_w] == True:
        player.x2speed = 1
        player.y2speed = 1

    if keys[pygame.K_a] == True:
        player.x1speed = 1
    else:
        player.x1speed = 0
    if keys[pygame.K_d] == True:
        player.x2speed = 1
    else:
        player.x2speed = 0
    if keys[pygame.K_s] == True:
        player.y1speed = 1
    else:
        player.y1speed = 0
    if keys[pygame.K_w] == True:
        player.y2speed = 1
    else:
        player.y2speed = 0

    if keys[pygame.K_ESCAPE] == True:
        pygame.quit(); sys.exit()
#-------------------------------------------------