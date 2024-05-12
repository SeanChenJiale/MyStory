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
from config import *
# import pygame.locals for easier 
# access to key coordinates
from pygame.locals import *



def draw_text(text,font,text_col,x,y):
    img = font.render(text,True,text_col)
    screen.blit(img,(x,y))

class Background(pygame.sprite.Sprite):
    def __init__(self, location):
        self.location = location
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load("./Assets/bg.png")
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

# initialize pygame
pygame.init()
screen = pygame.display.set_mode((MAPWIDTH, MAPHEIGHT))
slime1_Pos = [400,400]
# Define the dimensions of screen object

bg = Background((0,0))
# instantiate all square objects

user = player([100,100],25)
slime1 = slime(slime1_Pos)
group = [user,slime1]
# Variable to keep our game loop running
gameOn = True

tickcounter = 0
# Our game loop
clock = pygame.time.Clock()

while gameOn:
# for loop through the event queue
    
    for event in pygame.event.get():

        if event.type == KEYDOWN:
            # Define where the squares will appear on the screen
            # Use blit to draw them on the screen surface
            #if right arrow is pressed       
            if event.key == K_UP and user.location[1] > 0:
                user.facedir = "U"
                user.move_up()
                user.update(0)
                if user.rect.colliderect(slime1.rect):
                    screen.blit(bg.image,(bg.location))
                    screen.blit(slime1.images[0][0],slime1.location)
                    screen.blit(user.image,(user.location))
                    pygame.display.update()
                    pygame.time.delay(100)
                    user.move_down()
                    user.update(0)
                    
            if event.key == K_DOWN and user.location[1] < MAPHEIGHT - 50:
                user.facedir = "D"
                user.move_down()
                user.update(1)

                if user.rect.colliderect(slime1.rect):
                    screen.blit(bg.image,(bg.location))
                    screen.blit(user.image,(user.location))
                    screen.blit(slime1.images[0][1],slime1.location)
                    pygame.display.update()
                    pygame.time.delay(100)
                    user.move_up()
                    user.update(1)
                    
            if event.key == K_LEFT and user.location[0] > 0:
                user.facedir = "L"
                user.move_left()
                user.update(2)     

                if user.rect.colliderect(slime1.rect):
                    screen.blit(bg.image,(bg.location))
                    screen.blit(slime1.images[0][3],slime1.location)
                    screen.blit(user.image,(user.location))
                    pygame.display.update()
                    pygame.time.delay(100)
                    user.move_right()
                    user.update(2)

                    
                    
            if event.key == K_RIGHT and user.location[0] < MAPWIDTH - 50:
                user.facedir = "R"
                user.move_right() 
                user.update(3)
               
                if user.rect.colliderect(slime1.rect):
                    screen.blit(bg.image,(bg.location))
                    screen.blit(slime1.images[0][2],slime1.location)
                    screen.blit(user.image,(user.location))
                    pygame.display.update()
                    pygame.time.delay(100)
                    user.move_left()
                    user.update(3)
                    
                    
            if event.key == K_c :
                pass
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
        clock.tick(60)
        pygame.display.flip()            
    

