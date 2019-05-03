#-------------------------------------------------
"Importieren: Packages"
import pygame
import os
import sys
import random
pygame.init()
#-------------------------------------------------
"Erstellen: Display(Screen)"
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen.fill((255, 255, 255))
pygame.display.set_caption("Dodge Dungeon", "Dodge Dungeon")
#-------------------------------------------------
"Importieren: Gi"
import Gi as gi
#-------------------------------------------------
"Erstellen: Display(Screen)"
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen.fill((255, 255, 255))
pygame.display.set_caption("Dodge Dungeon", "Dodge Dungeon")
#-------------------------------------------------
"Klasse: Raum(Room)"
class Room():
    def __init__(self, size):
        self.size = size
        counter = self.size
        self.lvl = 0
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

    def room_victory(self):
        BLUE = (0, 0, 255)
        # -
        "Berechnung Ziel"
        winningminX = 860 - self.size * 40
        winningminY = 460 - self.size * 40
        winningmaxX = winningminX + 80
        winningmaxY = winningminY + 80
        winningrec = pygame.draw.rect(screen, BLUE,
                                      (winningmaxX, winningmaxY, winningmaxX - winningminX, winningmaxY - winningminY))
        # -
        if pygame.Rect.colliderect(winningrec, player1.hitbox) == True:
            player1.xPos = 920 + room.size * 40 - 50
            player1.yPos = 540 + room.size * 40 - 80
            self.lvl = self.lvl + 1
            trap_creation(traplist, 1)
            return self.lvl
#-------------------------------------------------
"Erstellen: Raum(Room)"
room = Room(6)
#-------------------------------------------------
"Klasse: Spieler(Player)"
class Player():
    def __init__(self, xPos, yPos, direction):
        "Positionen und Hitbox"
        self.xPos = xPos
        self.yPos = yPos
        self.direction = direction
        self.hitboxchanger = 0
        BLUE = (0, 255, 255)
        self.hitboxmaxX = 0
        self.hitboxminX = 0
        self.hitboxmaxY = 0
        self.hitboxminY = 0
        self.hitbox = pygame.draw.rect(screen, BLUE, (self.hitboxmaxX, self.hitboxmaxY, self.hitboxmaxX - self.hitboxminX, self.hitboxmaxY - self.hitboxminY))
        # -
        "Animationen"
        self.state = 0
        self.image = 0
        self.timer = 0
        # -
        "Bewegen"
        self.x1speed = 0
        self.x2speed = 0
        self.y1speed = 0
        self.y2speed = 0
        # -
        "Level"
        self.lvl = 0

    def player_blitting(self):
        direction = self.direction
        if self.image > 6:
            self.image = 6

        if direction == 0:
            screen.blit(gi.playerlist[self.image], (self.xPos, self.yPos))
            self.hitboxchanger = 0
        else:
            screen.blit(pygame.transform.flip(gi.playerlist[self.image], True, False), (self.xPos, self.yPos))
            self.hitboxchanger = 8

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
        self.hitboxmaxX = self.xPos + 40 + self.hitboxchanger
        self.hitboxminX = self.xPos + 5 + (self.hitboxchanger - 2)
        self.hitboxmaxY = self.yPos + 96
        self.hitboxminY = self.yPos + 116

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

    def player_hitbox(self):
        BLUE = (0, 0, 255)
        self.hitbox = pygame.draw.rect(screen, BLUE, (
        self.hitboxmaxX, self.hitboxmaxY, self.hitboxmaxX - self.hitboxminX, self.hitboxmaxY - self.hitboxminY))

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
"Erstellen: Spieler(Player)"
player1 = Player(850 + room.size*40, 440 + room.size*40, 0)
#-------------------------------------------------
"Klasse: Stachelfalle"
class SpikeTrap():
    def __init__(self, TrapNr, xPos, yPos):
        self.TrapNr = TrapNr
        self.xPos = xPos
        self.yPos = yPos
        self.image = 0
        self.state = 0
        self.timer = 0
        self.hitboxmaxX = self.xPos + 10
        self.hitboxminX = self.xPos - 50
        self.hitboxmaxY = self.yPos + 12
        self.hitboxminY = self.yPos - 12

    def trap_blitting(self):
        xPos = self.xPos
        yPos = self.yPos
        if self.TrapNr == 1:
            screen.blit(gi.spikelist[self.image], (xPos, yPos))

    def trap_hitbox(self):
        BLUE = (0, 0, 255)
        self.hitbox = pygame.draw.rect(screen, BLUE, (
            self.hitboxmaxX, self.hitboxmaxY, self.hitboxmaxX - self.hitboxminX, self.hitboxmaxY - self.hitboxminY))

    def trap_collision(self):
        if pygame.Rect.colliderect(self.hitbox, player1.hitbox) == True:
            player1.xPos = 920 + room.size*40 - 50
            player1.yPos = 540 + room.size*40 - 80
            self.state = 1

    def trap_animation(self):
        if self.state == 1:
            self.timer = self.timer + 1
            if self.timer == 20:
                self.image = self.image + 1
                self.timer = 0
            if self.image > 3:
                player1.xPos = 850 + room.size * 40
                player1.yPos = 440 + room.size * 40
                self.image = 0
                self.state = 0
#-------------------------------------------------
"Klasse: Laserfalle"
class LaserTrap():
    def __init__(self, xPos, yPos, direction):
        self.xPos = 920 + xPos*80
        self.yPos = 540 + yPos*80
        self.oldxPos = self.xPos
        self.oldyPos = self.yPos
        self.image = 0
        self.direction = direction
        self.difference = 0
        self.laserlist = []
        self.laserx = 0
        self.lasery = 0
        self.hitbox = 0
        self.hitboxdif = 0

    def laser_calculation(self):
        if self.direction == 1:
            self.image = 0
            self.difference = (475 + room.size * 40) - self.yPos
        if self.direction == 2:
            self.image = 1
            self.difference = (860 + room.size * 40) - self.xPos
        if self.direction == 3:
            self.image = 2
            self.difference = self.yPos - (540 - room.size * 40)
        if self.direction == 4:
            self.image = 3
            self.difference = self.xPos - (940 - room.size * 40)
        self.difference = int(self.difference/10)

        self.laserlist = [0]*self.difference


    def trap_blitting(self):
        screen.blit(gi.laserstatuelist[self.image], (self.xPos, self.yPos))

        if self.direction == 1:
            self.lasery = self.oldyPos + 60
            for ph in self.laserlist:
                self.lasery = self.lasery + 10
                screen.blit(gi.l6, (self.xPos + 30, self.lasery))
            self.hitboxdif = self.lasery - self.yPos

        elif self.direction == 2:
            self.laserx = self.oldxPos + 70
            for ph in self.laserlist:
                print(self.direction)
                self.laserx = self.laserx + 10
                screen.blit(gi.l5, (self.laserx, self.yPos + 40))
            self.hitboxdif = self.laserx - self.xPos

        elif self.direction == 3:
            self.lasery = self.oldyPos
            for ph in self.laserlist:
                print(self.direction)
                self.lasery = self.lasery - 10
                screen.blit(gi.l6, (self.xPos + 30, self.lasery))
            self.hitboxdif = self.lasery - self.yPos

        elif self.direction == 4:
            print("4")
            self.laserx = self.oldxPos
            for ph in self.laserlist:
                print(self.direction)
                self.laserx = self.laserx - 10
                screen.blit(gi.l5, (self.laserx, self.yPos + 40))
            self.hitboxdif = self.laserx - self.xPos

    def laser_hitbox(self):
        RED = (255, 0, 0)
        if self.direction == 1:
            self.hitbox = pygame.draw.rect(screen, RED, (self.xPos + 30, self.yPos + 70, 20, self.hitboxdif - 60))
        elif self.direction == 2:
            self.hitbox = pygame.draw.rect(screen, RED, (self.xPos + 80, self.yPos + 40, self.hitboxdif - 65, 20))
        elif self.direction == 3:
            self.hitbox = pygame.draw.rect(screen, RED, (self.xPos + 30, self.yPos, 20, self.hitboxdif))
        elif self.direction == 4:
            self.hitbox = pygame.draw.rect(screen, RED, (self.xPos, self.yPos + 40, self.hitboxdif, 20))

    def laser_collision(self):
        if pygame.Rect.colliderect(self.hitbox, player1.hitbox) == True:
            player1.xPos = 920 + room.size*40 - 50
            player1.yPos = 540 + room.size*40 - 80

lasertrap = LaserTrap(-1, -1, 1)
#-------------------------------------------------
"Funktion: Fallen erstellen"
def trap_creation(list, number):
    counter = 0
    phlist = [0]*number
    for ph in phlist:
        ph = SpikeTrap(1, random.randint(940 - room.size*40, 840 + room.size*40), random.randint(540 - room.size*40, 440 + room.size*40))
        print(ph)
        list.append(ph)
        counter = counter + 1
#-
"Erstellen: Fallen-Liste"
traplist = []
#-------------------------------------------------
"Funktion: Schichten(Layers) anzeigen"
def layer_blitting():
    "Layer 1 (unterste)"
    lasertrap.laser_calculation()
    lasertrap.laser_hitbox()
    room.room_victory()
    player1.player_hitbox()
    room.room_blitting()
    #-
    "Layer 2 (mittlere)"
    for ph in traplist:
        ph.trap_hitbox()
        ph.trap_blitting()
        ph.trap_collision()
        ph.trap_animation()
    lasertrap.trap_blitting()
    lasertrap.laser_collision()
    #-
    "Layer 3 (oberste)"
    player1.player_movement()
    player1.player_animation()
    player1.player_collision()
    player1.player_blitting()
    #-
    "Display updaten"
    pygame.display.flip()
#-------------------------------------------------
"Klasse: Knopf"
class button():
    def __init__(self, imagelist, image, animation, xPos, yPos, heigth, length):
        self.imagelist = imagelist
        self.image = image
        self.animation = animation
        self.xPos = xPos
        self.yPos = yPos
        self.heigth = heigth
        self.length = length
        self.command = 0
        self.oldlength = self.length
        self.oldheigth = self.heigth

    def button_blitting(self):
        screen.blit(self.imagelist[self.image], (self.xPos - self.length/2, self.yPos - self.heigth/2))
        self.length = self.oldlength
        self.heigth = self.oldheigth

    def button_clicking(self):
        mouseposX, mouseposY = pygame.mouse.get_pos()
        if mouseposX > self.xPos - self.oldlength/2 and mouseposY > self.yPos - self.oldheigth/2 \
        and mouseposX < self.xPos + self.oldlength/2 and mouseposY < self.yPos + self.oldheigth/2:
            mouseclick = pygame.mouse.get_pressed()
            if mouseclick == (1, 0, 0):
                self.command = 1
                return self.command

    def button_animation(self):
        if self.animation == 1:
            mouseposX, mouseposY = pygame.mouse.get_pos()
            if mouseposX > self.xPos - self.oldlength / 2 and mouseposY > self.yPos - self.oldheigth / 2 \
            and mouseposX < self.xPos + self.oldlength / 2 and mouseposY < self.yPos + self.oldheigth / 2:
                self.length = int(self.length + self.length/5)
                self.heigth = int(self.heigth + self.heigth/5)
                gi.resize(gi.buttonlist, self.length, self.heigth)
            else:
                gi.resize(gi.buttonlist, self.length, self.heigth)
        else:
            if self.animation == 2:
                pass
#-------------------------------------------------
"Erstellen: Menü-Knöpfe"
startbutton = button(gi.buttonlist, 0, 1, 960, 440, 90, 300)
settingsbutton = button(gi.buttonlist, 1, 1, 960, 540, 90, 300)
exitbutton = button(gi.buttonlist, 2, 1, 960, 640, 90, 300)
menubuttonlist = [startbutton, settingsbutton, exitbutton]
#-------------------------------------------------
def button_execution(name):
    if name == startbutton:
        if startbutton.command == 1:
            global maingameloop
            maingameloop = True
            global menuloop
            menuloop = False
            startbutton.command = 0
    if name == settingsbutton:
        if settingsbutton.command == 1:
            print("hi")
            settingsbutton.command = 0
    if name == exitbutton:
        if exitbutton.command == 1:
            pygame.quit(); sys.exit()
#-------------------------------------------------
"Funktion: Menü-Programm"
def menu_runner():
    for ph in menubuttonlist:
        ph.button_animation()
        ph.button_clicking()
        ph.button_blitting()
        button_execution(ph)
    pygame.display.flip()
    screen.fill((255, 255, 255))
#-------------------------------------------------
maingameloop = True
menuloop = False
"Funktion: Tastatureingabe abfragen"
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
        global maingameloop
        maingameloop = False
        global menuloop
        menuloop = True
#-------------------------------------------------