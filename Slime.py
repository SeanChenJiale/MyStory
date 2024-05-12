# -*- coding: utf-8 -*-
"""
Created on Sun May 12 12:39:57 2024

@author: zacwo
"""
import pygame
class slime(pygame.sprite.Sprite):
    def __init__(self, location):
        pygame.sprite.Sprite.__init__(self)
        self.location = location
        self.image = pygame.image.load("./Assets/slimer.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.surf = pygame.Surface((50, 50))
        