import pygame
import sys
pygame.init()
screen = pygame.display.set_mode((1000, 1000), pygame.RESIZABLE)
loop = True
while loop == True:
    pygame.event.pump()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and keys[pygame.K_w] == True:
        print("Saletti")

    if keys[pygame.K_ESCAPE] == True:
        pygame.quit(); sys.exit()
