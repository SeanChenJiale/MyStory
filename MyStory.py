# -*- coding: utf-8 -*-
"""
Created on Thu May  9 09:11:47 2024

@author: ChenS11
"""

# import the pygame module
import pygame
import sys
# import pygame.locals for easier 
# access to key coordinates
from pygame.locals import *

def checkCollision(sprite1, sprite2):
    col = sprite1.rect.collide_rect(sprite2.rect)
    if col == True:
        return True
class Background(pygame.sprite.Sprite):
    def __init__(self, location):
        self.location = location
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load("C:/RPGgame/Assets/bg.png")
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
# Define our square object and call super to
# give it all the properties and methods of pygame.sprite.Sprite
# Define the class for our square objects
class Square(pygame.sprite.Sprite):
	def __init__(self):
		super(Square, self).__init__()        
		self.prevmove = " "		
		# Define the dimension of the surface
		# Here we are making squares of side 25px
		self.surf = pygame.Surface((50, 50))
		# Define the color of the surface using RGB color coding.
		self.surf.fill((0, 200, 255))
		self.rect = self.surf.get_rect()
class slime(pygame.sprite.Sprite):
    def __init__(self, location):
        pygame.sprite.Sprite.__init__(self)
        self.location = location
        self.image = pygame.image.load("C:/RPGgame/Assets/slimer.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.surf = pygame.Surface((50, 50))
        
class player(pygame.sprite.Sprite):
    def __init__(self, location,movedist):
        pygame.sprite.Sprite.__init__(self)
        self.movedist = movedist
        self.prevmove = " "
        self.location = location
        self.user_backgrounder_location = location
        ### images is a collection of lists of animations of 4 directions,
        ### in the order, [up],[down],[left],[right]
        self.images = []
        self.movelist = []
        #adding all the images to sprite array
        self.images.append(
            [pygame.image.load("C:/RPGgame/Assets/playerasset/player_up1.png"),
            pygame.image.load("C:/RPGgame/Assets/playerasset/player_up2.png")])
        self.images.append(
            [pygame.image.load("C:/RPGgame/Assets/playerasset/player_down1.png"),
            pygame.image.load("C:/RPGgame/Assets/playerasset/player_down2.png")])
        self.images.append(
            [pygame.image.load("C:/RPGgame/Assets/playerasset/player_left1.png"),
            pygame.image.load("C:/RPGgame/Assets/playerasset/player_left2.png")])
        self.images.append(
            [pygame.image.load("C:/RPGgame/Assets/playerasset/player_right1.png"),
            pygame.image.load("C:/RPGgame/Assets/playerasset/player_right2.png")])
        self.imageidle = pygame.image.load("C:/RPGgame/Assets/playerasset/player_downidle.png")
        #index value to get the image from the array
        #initially it is 0 
        self.index = 0
        #now the image that we will display will be the index from the image array 
        self.image = self.imageidle
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.surf = pygame.Surface((50, 50))
    def update(self,direction):
        """ direction is encoded in index up down left right"""
        currImgList = self.images[direction]
        #when the update method is called, we will increment the index
        self.index += 1
        
        #if the index is larger than the total images
        if self.index >= len(currImgList):
            #we will make the index to 0 again
            self.index = 0
        
        #finally we will update the image that will be displayed
        self.image = currImgList[self.index]
    def position_returner(keyword,xypos,movement_jump):
        """ Args : keyword, takes in U D L R
        
        pos : takes in current pos 
        
        movement_jump : is the jump of a singular direction
        
        returns change in position"""
        if keyword == "L":
            xypos[0] -= movement_jump
            return xypos
        if keyword == "R":
            xypos[0] += movement_jump
            return xypos
        if keyword == "D":
            xypos[1] += movement_jump
            return xypos
        if keyword == "U":
            xypos[1] -= movement_jump
            return xypos

# initialize pygame
pygame.init()

MAPWIDTH = 800
MAPHEIGHT = 600
slime1_Pos = [400,400]
# Define the dimensions of screen object
screen = pygame.display.set_mode((MAPWIDTH, MAPHEIGHT))
bg = Background((0,0))
# instantiate all square objects

user = player([100,100],25)
slime1 = slime(slime1_Pos)
user_shadow = Square()
user_shadow.surf.fill((0, 0, 0))

group = [user,slime1]
# Variable to keep our game loop running
gameOn = True


# Our game loop
while gameOn:
    clock = pygame.time.Clock()
    
    # for loop through the event queue
    for event in pygame.event.get():

        if event.type == KEYDOWN:
            # Define where the squares will appear on the screen
            # Use blit to draw them on the screen surface
            #if right arrow is pressed
            
            if event.key == K_UP and user.location[1] > 0:
                user.update(0)
                user.prevmove = "U"
                user.location[1] -= user.movedist
                
            if event.key == K_DOWN and user.location[1] < MAPHEIGHT - 50:
                user.update(1)
                user.prevmove = "D"
                user.location[1] += user.movedist
                 
            if event.key == K_LEFT and user.location[0] > 0:
                user.update(2)     
                user.prevmove = "L"
                user.location[0] -= user.movedist
                
            if event.key == K_RIGHT and user.location[0] < MAPWIDTH - 50:
                user.update(3)
                user.prevmove = "R"
                user.location[0] += user.movedist
                
			# If the Backspace key has been pressed set
			# running to false to exit the main loop
            if event.key == K_BACKSPACE:
                pygame.quit()
                sys.exit()
                gameOn = False	
            
    		# Check for QUIT event
            elif event.type == QUIT:
                pygame.quit()
                sys.exit()
                gameOn = False

        screen.blit(bg.image,(bg.location))
        screen.blit(user.image,(user.location))
        screen.blit(slime1.image,(slime1.location))
        	# Update the display using flip
        pygame.display.update()
        clock.tick(30)
        pygame.display.flip()            
    

