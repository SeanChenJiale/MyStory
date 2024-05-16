# -*- coding: utf-8 -*-
"""
Created on Thu May  9 09:11:47 2024

@author: ChenS11
"""
# import the pygame 
from Player import player
from Slime import slime
from Background import background
from Block import *
import pygame
import sys
from config import *
# import pygame.locals for easier 
# access to key coordinates
from pygame.locals import *
from random import randrange




class spritesheet:
    def __init__(self,path):
        self.spritesheet = pygame.image.load(path).convert_alpha()
    def get_image(self,x,y,width,height):
        sprite = pygame.Surface([width,height])
        sprite.blit(self.spritesheet,(0,0),(x,y,width,height))
        sprite.set_colorkey(black)

        
        return sprite #it is returning a surface. 
class game:
    def __init__(self):
        self.screen = pygame.display.set_mode((MAPWIDTH, MAPHEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.terrain_spritesheet = spritesheet('./Assets/terrainspritesheet.png')
        self.player_spritesheet = spritesheet('./Assets/playerasset/playerspritesheet.png')
        self.slime_spritesheet = spritesheet('./Assets/slime/slimespritesheet.png')
    def create_tile_map(self):
        for i in range(int(MAPHEIGHT/25)):
            for j in range(int(MAPWIDTH/25)):
                texture_gen = randrange(12)
                match texture_gen:
                    case 0:
                        grass3_1(self,j,i)                       
                    case 1:
                        grass2_1(self,j,i)
                    case 2:
                        grass3_1(self,j,i) 
                    case 3:
                        grass3_2(self,j,i) 
                    case 4:
                        grass2_1(self,j,i)
                    case 5:
                        grass2_2(self,j,i)  
                    case 6:
                        grass2_3(self,j,i)  
                    case 7:
                        grass2_4(self,j,i)      
                    case 8:
                        grass3_1(self,j,i)   
                    case 9:
                        grass3_2(self,j,i)
                    case 10:
                        grass3_3(self,j,i)   
                    case 11:
                        grass3_4(self,j,i)   
        for i,row in enumerate(tilemap):
            for j,col in enumerate(row):

                match col: 
                    case "S":
                        self.slime = slime(self,j,i)
                        
                    case "P":
                        self.player = player(self,j,i)

                    case "1":
                        tree3x3_1(self, j, i)
                        
                    case "2":
                        tree3x3_2(self, j, i)
                        
                    case "3":
                        tree3x3_3(self, j, i)

                    case "4":
                        grass1(self, j, i)
                        tree3x3_4(self, j, i)

                    case "5":
                        grass1(self, j, i)
                        tree3x3_5(self, j, i)

                    case "6":
                        grass1(self, j, i)
                        tree3x3_6(self, j, i)

                    case "7":
                        grass1(self, j, i)
                        tree3x3_7(self, j, i)

                    case "8":
                        grass1(self, j, i)
                        tree3x3_8(self, j, i)

                    case "9":
                        grass1(self, j, i)
                        tree3x3_9(self, j, i)

    def create(self):
        # initialize pygame
        self.all_sprites = pygame.sprite.LayeredUpdates() 
        self.blocks = pygame.sprite.LayeredUpdates()
        self.create_tile_map()

    def update(self):
        self.all_sprites.update() #call update to get all the changes in all sprites
        # then draw all again.
             
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_p]:
                self.running = False
    
    def draw(self):
        self.screen.fill(black)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()
    
    def main(self):
        while self.running:
            self.events()
            self.update()
            self.draw()



game = game()
game.create()

while game.running:
    game.main()

pygame.quit()
sys.exit()



        
    

