# -*- coding: utf-8 -*-
"""
Created on Sun May 12 22:26:01 2024

@author: zacwo
"""
import pygame

class background(pygame.sprite.Sprite):
    def __init__(self, location):
        self.location = location
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load("./Assets/bg.png")
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location