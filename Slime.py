# -*- coding: utf-8 -*-
"""
Created on Sun May 12 12:39:57 2024

@author: zacwo
"""
import pygame
class slime(pygame.sprite.Sprite):
    def __init__(self, location):
        self.images = []
        pygame.sprite.Sprite.__init__(self)
        self.location = location
        self.image = pygame.image.load("./Assets/slime/slime_idle.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

        self.images.append(
            [pygame.image.load("./Assets/slime/slime_walkfront.png"),
            pygame.image.load("./Assets/slime/slime_walkfront.png"),
            pygame.image.load("./Assets/slime/slime_walkleft.png"),
            pygame.image.load("./Assets/slime/slime_walkright.png")])
              