# -*- coding: utf-8 -*-
"""
Created on Sun May 12 12:37:28 2024

@author: zacwo
"""
import pygame
class player(pygame.sprite.Sprite):
    def __init__(self, location,movedist):
        pygame.sprite.Sprite.__init__(self)
        self.movedist = movedist
        self.facedir = " "
        self.location = location
        ### images is a collection of lists of animations of 4 directions,
        ### in the order, [up],[down],[left],[right]
        self.images = []
        #adding all the images to sprite array
        self.images.append(
            [pygame.image.load("./Assets/playerasset/player_up1.png"),
            pygame.image.load("./Assets/playerasset/player_up2.png")])
        self.images.append(
            [pygame.image.load("./Assets/playerasset/player_down1.png"),
            pygame.image.load("./Assets/playerasset/player_down2.png")])
        self.images.append(
            [pygame.image.load("./Assets/playerasset/player_left1.png"),
            pygame.image.load("./Assets/playerasset/player_left2.png")])
        self.images.append(
            [pygame.image.load("./Assets/playerasset/player_right1.png"),
            pygame.image.load("./Assets/playerasset/player_right2.png")])
        self.image = pygame.image.load("./Assets/playerasset/player_downidle.png")
        #index value to get the image from the array
        #initially it is 0 
        self.index = 0
        #now the image that we will display will be the index from the image array 
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = self.location
        
    def update(self,direction):
        """ direction is encoded in index up down left right"""
        currImgList = self.images[direction]
        #when the update method is called, we will increment the index
        self.index += 1
        
        #if the index is larger than the total images
        if self.index >= len(currImgList):
            #we will make the index to 0 again
            self.index = 0
        
        #finally we will update the image that will be displayed
        self.image = currImgList[self.index]
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = self.location
        

    def move_up(self):

        self.location[1] -= self.movedist
        
    def move_down(self):

        self.location[1] += self.movedist
        
    def move_left(self):

        self.location[0] -= self.movedist
        
    def move_right(self):

        self.location[0] += self.movedist
    

            
