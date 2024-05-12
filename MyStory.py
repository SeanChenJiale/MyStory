# -*- coding: utf-8 -*-
"""
Created on Thu May  9 09:11:47 2024

@author: ChenS11
"""
# import the pygame 
from Player import player
from Slime import slime
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
        self.image = pygame.image.load("./Assets/bg.png")
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

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
    

