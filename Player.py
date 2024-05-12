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
        self.prevmove = " "
        self.location = location
        self.user_backgrounder_location = location
        ### images is a collection of lists of animations of 4 directions,
        ### in the order, [up],[down],[left],[right]
        self.images = []
        self.movelist = []
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
        self.imageidle = pygame.image.load("./Assets/playerasset/player_downidle.png")
        #index value to get the image from the array
        #initially it is 0 
        self.index = 0
        #now the image that we will display will be the index from the image array 
        self.image = self.imageidle
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.surf = pygame.Surface((50, 50))
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
    def position_returner(keyword,xypos,movement_jump):
        """ Args : keyword, takes in U D L R
        
        pos : takes in current pos 
        
        movement_jump : is the jump of a singular direction
        
        returns change in position"""
        if keyword == "L":
            xypos[0] -= movement_jump
            return xypos
        if keyword == "R":
            xypos[0] += movement_jump
            return xypos
        if keyword == "D":
            xypos[1] += movement_jump
            return xypos
        if keyword == "U":
            xypos[1] -= movement_jump
            return xypos
