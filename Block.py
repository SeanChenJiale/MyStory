# -*- coding: utf-8 -*-
"""
Created on Sun May 12 23:33:10 2024

@author: zacwo
"""
import pygame
from config import TILESIZE
class block(pygame.sprite.Sprite):
    def __init__ (self, game, x, y):
        self.game = game
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        
        self.width = TILESIZE
        self.height = TILESIZE