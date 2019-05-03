#-------------------------------------------------
"Importieren: Packages"
import pygame
import os
import sys
pygame.init()
#-------------------------------------------------
"Importieren: Funktionen(Functions)"
import Functions as fc
#-------------------------------------------------
"Loop"
while True:
    maingameloop = fc.maingameloop
    menuloop = fc.menuloop
    if menuloop == True:
        fc.keyinput(fc.player1)
        fc.menu_runner()
    #-
    if maingameloop == True:
        fc.keyinput(fc.player1)
        fc.layer_blitting()
#-------------------------------------------------