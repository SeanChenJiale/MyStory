# -*- coding: utf-8 -*-
"""
Created on Sun May 12 12:39:57 2024

@author: zacwo
"""
import pygame
from config import *
class slime(pygame.sprite.Sprite):
    def __init__ (self, game, x, y):
        
        self.game = game
        self._layer = PLAYER_LAYER - 1
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x * TILESIZE 
        self.y = y * TILESIZE 
        
        self.direction = 1
        
        self.width = TILESIZE 
        self.height = TILESIZE 
        
        self.image = self.game.slime_spritesheet.get_image(0,0,self.width,self.height)
        self.rect = self.image.get_rect() # able to get x and y coordinates.
        self.rect.x = self.x
        self.rect.y = self.y
        
        self.x_change = 0
        self.y_change = 0
    def update(self):
        pass