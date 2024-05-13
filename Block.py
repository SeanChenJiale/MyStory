# -*- coding: utf-8 -*-
"""
Created on Sun May 12 23:33:10 2024

@author: zacwo
"""
import pygame
from config import *

class grass1(pygame.sprite.Sprite):
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
        

class grass2(pygame.sprite.Sprite):
    def __init__ (self, game, x, y):
        
        self.game = game
        self._layer = GROUND_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        
        self.width = TILESIZE
        self.height = TILESIZE
        
        self.image = self.game.terrain_spritesheet.get_image(0,50,self.width,self.height)
        self.rect = self.image.get_rect() # able to get x and y coordinates.
        self.rect.x = self.x
        self.rect.y = self.y
        
class tree_tl(pygame.sprite.Sprite):
    def __init__ (self, game, x, y):
        
        self.game = game
        self._layer = BLOCKS_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x * TILESIZE 
        self.y = y * TILESIZE 
        
        self.width = TILESIZE 
        self.height = TILESIZE 
        
        self.image = self.game.terrain_spritesheet.get_image(100,0,self.width,self.height)
        self.rect = self.image.get_rect() # able to get x and y coordinates.
        self.rect.x = self.x
        self.rect.y = self.y

class tree_tr(pygame.sprite.Sprite):
    def __init__ (self, game, x, y):
        
        self.game = game
        self._layer = BLOCKS_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x * TILESIZE 
        self.y = y * TILESIZE 
        
        self.width = TILESIZE 
        self.height = TILESIZE 
        
        self.image = self.game.terrain_spritesheet.get_image(150,0,self.width,self.height)
        self.rect = self.image.get_rect() # able to get x and y coordinates.
        self.rect.x = self.x
        self.rect.y = self.y
        
class tree_bl(pygame.sprite.Sprite):
    def __init__ (self, game, x, y):
        
        self.game = game
        self._layer = BLOCKS_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x * TILESIZE 
        self.y = y * TILESIZE 
        
        self.width = TILESIZE 
        self.height = TILESIZE 
        
        self.image = self.game.terrain_spritesheet.get_image(100,50,self.width,self.height)
        self.rect = self.image.get_rect() # able to get x and y coordinates.
        self.rect.x = self.x
        self.rect.y = self.y
        
class tree_br(pygame.sprite.Sprite):
    def __init__ (self, game, x, y):
        
        self.game = game
        self._layer = BLOCKS_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x * TILESIZE 
        self.y = y * TILESIZE 
        
        self.width = TILESIZE 
        self.height = TILESIZE 
        
        self.image = self.game.terrain_spritesheet.get_image(150,50,self.width,self.height)
        self.rect = self.image.get_rect() # able to get x and y coordinates.
        self.rect.x = self.x
        self.rect.y = self.y