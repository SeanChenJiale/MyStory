# -*- coding: utf-8 -*-
"""
Created on Sun May 12 23:33:10 2024

@author: zacwo
"""
import pygame
from config import *
class basetile(pygame.sprite.Sprite):
    def __init__ (self, game, x, y):
        
        self.game = game
        self._layer = GROUND_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        
        self.width = TILESIZE
        self.height = TILESIZE
        self.image = self.game.terrain_spritesheet.get_image(0,0,self.width,self.height)
        
        self.rect = self.image.get_rect() # able to get x and y coordinates.
        self.rect.x = self.x
        self.rect.y = self.y
        
class grass1(basetile):
    def __init__ (self, game, x, y):
        """
        we have a super class called basetile it contains all important variables
        to prevent from confusing code, super() has been used to call parent class 
        in each child class 
        """
        super().__init__(game, x, y)
        self.image = self.game.terrain_spritesheet.get_image(0,0,self.width,self.height)

class grass2(basetile):
    def __init__ (self, game, x, y):
        super().__init__(game, x, y)
        self.image = self.game.terrain_spritesheet.get_image(0,50,self.width,self.height)

class grass3(basetile):
    def __init__ (self, game, x, y):
        super().__init__(game, x, y)
        self.image = self.game.terrain_spritesheet.get_image(0,100,self.width,self.height)

        
class tree3x3_1(basetile):
    def __init__ (self, game, x, y):
        super().__init__(game, x, y)
        self.image = self.game.terrain_spritesheet.get_image(50,0,self.width,self.height)
        
class tree3x3_2(basetile):
    def __init__ (self, game, x, y):
        super().__init__(game, x, y)
        self.image = self.game.terrain_spritesheet.get_image(100,0,self.width,self.height)

class tree3x3_3(basetile):
    def __init__ (self, game, x, y):
        super().__init__(game, x, y)
        self.image = self.game.terrain_spritesheet.get_image(150,0,self.width,self.height)

class tree3x3_4(basetile):
    def __init__ (self, game, x, y):
        super().__init__(game, x, y)
        self.image = self.game.terrain_spritesheet.get_image(50,50,self.width,self.height)

class tree3x3_5(basetile):
    def __init__ (self, game, x, y):
        super().__init__(game, x, y)
        self.image = self.game.terrain_spritesheet.get_image(100,50,self.width,self.height)

class tree3x3_6(basetile):
    def __init__ (self, game, x, y):
        super().__init__(game, x, y)
        self.image = self.game.terrain_spritesheet.get_image(150,50,self.width,self.height)

class tree3x3_7(basetile):
    def __init__ (self, game, x, y):
        super().__init__(game, x, y)
        self.image = self.game.terrain_spritesheet.get_image(50,100,self.width,self.height)

class tree3x3_8(basetile):
    def __init__ (self, game, x, y):
        super().__init__(game, x, y)
        self.image = self.game.terrain_spritesheet.get_image(100,100,self.width,self.height)

class tree3x3_9(basetile):
    def __init__ (self, game, x, y):
        super().__init__(game, x, y)
        self.image = self.game.terrain_spritesheet.get_image(150,100,self.width,self.height)

