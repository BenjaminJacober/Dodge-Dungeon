#-------------------------------------------------
"Importieren von Packages"
import pygame
import os
import sys
pygame.init()
#-------------------------------------------------
"Resize Funktion"
def resize(list, size1, size2):
    counter = 0
    for ph in list:
        ph = pygame.transform.scale(ph, (size1, size2))
        list[counter] = ph
        counter = counter + 1
#-------------------------------------------------
"Floor Tiles initalisieren"
f1 = pygame.image.load(os.path.join("Images", "FloorTile (1).png")).convert_alpha()
f2 = pygame.image.load(os.path.join("Images", "FloorTile (2).png")).convert_alpha()
f3 = pygame.image.load(os.path.join("Images", "FloorTile (3).png")).convert_alpha()
f4 = pygame.image.load(os.path.join("Images", "FloorTile (4).png")).convert_alpha()
f5 = pygame.image.load(os.path.join("Images", "FloorTile (5).png")).convert_alpha()
f6 = pygame.image.load(os.path.join("Images", "FloorTile (6).png")).convert_alpha()
f7 = pygame.image.load(os.path.join("Images", "FloorTile (7).png")).convert_alpha()
f8 = pygame.image.load(os.path.join("Images", "FloorTile (8).png")).convert_alpha()

floorlist = [f1, f2, f3, f4, f5, f6, f7, f8]
resize(floorlist, 80, 80)
#-------------------------------------------------
"Walls initialisieren"
w1 = pygame.image.load(os.path.join("Images", "Wall (1).png")).convert_alpha()
w2 = pygame.image.load(os.path.join("Images", "Wall (2).png")).convert_alpha()
w3 = pygame.image.load(os.path.join("Images", "Wall (3).png")).convert_alpha()

walllist = [w1, w2, w3]
resize(walllist, 80, 100)
#-------------------------------------------------
"WallsY initialisieren"
wy1 = pygame.image.load(os.path.join("Images", "WallY (1).png")).convert_alpha()
wy3 = pygame.image.load(os.path.join("Images", "WallY (3).png")).convert_alpha()
wy4 = pygame.image.load(os.path.join("Images", "WallY (4).png")).convert_alpha()

wally1list = [wy1, wy3, wy4]
resize(wally1list, 35, 100)
#-
wy2 = pygame.image.load(os.path.join("Images", "WallY (2).png")).convert_alpha()

wally2list = [wy2]
resize(wally2list, 35, 80)
#-------------------------------------------------
"Player initialisieren"

p1 = pygame.image.load(os.path.join("Images", "PlayerStanding (1).png")).convert_alpha()
p2 = pygame.image.load(os.path.join("Images", "PlayerStanding (2).png")).convert_alpha()
p3 = pygame.image.load(os.path.join("Images", "PlayerStanding (3).png")).convert_alpha()
p4 = pygame.image.load(os.path.join("Images", "PlayerRunning (1).png")).convert_alpha()
p5 = pygame.image.load(os.path.join("Images", "PlayerRunning (2).png")).convert_alpha()
p6 = pygame.image.load(os.path.join("Images", "PlayerRunning (3).png")).convert_alpha()
p7 = pygame.image.load(os.path.join("Images", "PlayerRunning (4).png")).convert_alpha()

playerlist = [p1, p2, p3, p4, p5, p6, p7]
resize(playerlist, 128, 128)
#-------------------------------------------------
"Fallen initialisieren"

"Spikes"

sp1 = pygame.image.load(os.path.join("Images", "Spikes (1).png")).convert_alpha()
sp2 = pygame.image.load(os.path.join("Images", "Spikes (2).png")).convert_alpha()
sp3 = pygame.image.load(os.path.join("Images", "Spikes (3).png")).convert_alpha()
sp4 = pygame.image.load(os.path.join("Images", "Spikes (4).png")).convert_alpha()

spikelist = [sp1, sp2, sp3, sp4]
resize(spikelist, 80, 80)
#-

"Laserfalle"

l1 = pygame.image.load(os.path.join("Images", "StatueLaserInactive.png")).convert_alpha()
l2 = pygame.image.load(os.path.join("Images", "StatueLaserActive.png")).convert_alpha()
l3 = pygame.image.load(os.path.join("Images", "StatueBack.png")).convert_alpha()
l4 = pygame.image.load(os.path.join("Images", "StatueSide.png")).convert_alpha()
l5 = pygame.image.load(os.path.join("Images", "StatueLaserX.png")).convert_alpha()
l6 = pygame.image.load(os.path.join("Images", "StatueLaserY.png")).convert_alpha()

laserstatuelist = [l1, l4, l3, l4]
resize(laserstatuelist, 80, 100)
l5 = pygame.transform.scale(l5, (10, 20))
l6 = pygame.transform.scale(l6, (20, 10))
#-------------------------------------------------
"Menü Knöpfe initialisieren"

stb = pygame.image.load(os.path.join("Images", "StartButton.png")).convert_alpha()
seb = pygame.image.load(os.path.join("Images", "SettingsButton.png")).convert_alpha()
exb = pygame.image.load(os.path.join("Images", "ExitButton.png")).convert_alpha()

buttonlist = [stb, seb, exb]
resize(buttonlist, 300, 90)
