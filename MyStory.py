# -*- coding: utf-8 -*-
"""
Created on Thu May  9 09:11:47 2024

@author: ChenS11
"""
# import the pygame 
from Player import player
from Slime import slime
from Background import background
import pygame
import sys
from config import *
# import pygame.locals for easier 
# access to key coordinates
from pygame.locals import *



def draw_text(text,font,text_col,x,y):
    img = font.render(text,True,text_col)
    screen.blit(img,(x,y))

class spritesheet:
    def __init__(self):
        self.spritesheet = "PLACEHOLDER"
class game:
    def __init__(self):
        self.screen = pygame.display.set_mode((MAPWIDTH, MAPHEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
    def createTilemap(self):
        pass
    
    def create(self):
        # initialize pygame
        pygame.init()

        self.slime1_Pos = [400,400]
        self.slime2_Pos = [500,500]
        # Define the dimensions of screen object

        self.bg = background((0,0))
        # instantiate all square objects

        self.user = player([100,100],25)
        self.slime1 = slime(self.slime1_Pos)
        self.slime2 = slime(self.slime2_Pos)
        self.enemies = [self.slime1,self.slime2]
        pass
    
    def update(self):
        pass
    
    def events(self):
        pass
    
    def draw(self):
        pass 
    
    def main(self):
         for event in pygame.event.get():

             if event.type == KEYDOWN:
                 # Define where the squares will appear on the screen
                 # Use blit to draw them on the screen surface
                 #if right arrow is pressed       
                 if event.key == K_UP and self.user.location[1] > 0:
                     self.user.facedir = "U"
                     self.user.move_up()
                     self.user.update(0)
                     for enemy in self.enemies:
                         if self.user.rect.colliderect(enemy.rect):
                             self.screen.blit(self.bg.image,(self.bg.location))
                             self.screen.blit(self.slime1.images[0][0],self.slime1.location)
                             self.screen.blit(self.user.image,(self.user.location))
                             pygame.display.update()
                             pygame.time.delay(FPS)
                             self.user.move_down()
                             self.user.update(0)
                             
                 if event.key == K_DOWN and self.user.location[1] < MAPHEIGHT - 50:
                     self.user.facedir = "D"
                     self.user.move_down()
                     self.user.update(1)
                     for enemy in self.enemies:
                         if self.user.rect.colliderect(enemy.rect):
                             self.screen.blit(self.bg.image,(self.bg.location))
                             self.screen.blit(self.user.image,(self.user.location))
                             self.screen.blit(self.slime1.images[0][1],self.slime1.location)
                             pygame.display.update()
                             pygame.time.delay(FPS)
                             self.user.move_up()
                             self.user.update(1)
                         
                 if event.key == K_LEFT and self.user.location[0] > 0:
                     self.user.facedir = "L"
                     self.user.move_left()
                     self.user.update(2)     
                     for enemy in self.enemies:
                         if self.user.rect.colliderect(enemy.rect):
                             self.screen.blit(self.bg.image,(self.bg.location))
                             self.screen.blit(self.slime1.images[0][3],self.slime1.location)
                             self.screen.blit(self.user.image,(self.user.location))
                             pygame.display.update()
                             pygame.time.delay(FPS)
                             self.user.move_right()
                             self.user.update(2)

                         
                         
                 if event.key == K_RIGHT and self.user.location[0] < MAPWIDTH - 50:
                     self.user.facedir = "R"
                     self.user.move_right() 
                     self.user.update(3)
                     for enemy in self.enemies:
                         if self.user.rect.colliderect(enemy.rect):
                             self.screen.blit(self.bg.image,(self.bg.location))
                             self.screen.blit(self.slime1.images[0][2],self.slime1.location)
                             self.screen.blit(self.user.image,(self.user.location))
                             pygame.display.update()
                             pygame.time.delay(FPS)
                             self.user.move_left()
                             self.user.update(3)
                             
                         
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

             self.screen.blit(self.bg.image,(self.bg.location))
             self.screen.blit(self.user.image,(self.user.location))
             self.screen.blit(self.slime1.image,(self.slime1.location))
             self.screen.blit(self.slime2.image,(self.slime2.location))
             	# Update the display using flip

         pygame.display.update()
         self.clock.tick(FPS)
         pygame.display.flip()    


game = game()
game.create()

while game.running:
    game.main()

pygame.quit()
sys.exit()



        
    

