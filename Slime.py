# -*- coding: utf-8 -*-
"""
Created on Sun May 12 12:39:57 2024

@author: Sean
"""
import pygame
from config import *
import random
class slime(pygame.sprite.Sprite):
    def match_walk_ani(self,walkanimationlist):
        match self.walkcycle:
            case 0:
                self.image = walkanimationlist[self.walkcycle]
                self.walkcycle +=1
            
            case 1:
                self.image = walkanimationlist[self.walkcycle]
                self.walkcycle +=1

            case 2:
                self.image = walkanimationlist[self.walkcycle - 1] ## slime delayani
                self.walkcycle = -1
                
    def __init__ (self, game, x, y):
        self.slimestep = 25
        self.game = game
        self._layer = PLAYER_LAYER - 1
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x * TILESIZE 
        self.y = y * TILESIZE 
        
        self.direction = random.choice([0,1,2,3])
        
        self.width = TILESIZE 
        self.height = TILESIZE 
        
        self.image = self.game.slime_spritesheet.get_image(0,0,self.width,self.height)

        self.lastattackanimation = 0
        self.lastwalkanimation = 0
        self.lastchangestrafe = 0
        self.strafechangedelay = 400
        self.attackcooldown = 0
        self.animationdelay = 150 #default animation delay.
        self.walkdelay = 400 # default tick delay.
        self.debuffdelay = 0
        self.walkcycle = -1
        self.attackcycle = -1 # default values 
        self.now = 0 # self.now is a counter to get the current game tick in pygame

        self.isstrafe = False
        self.isidle = True
        self.isattacking = False
        self.maxheatlh = 100
        self.currenthealth = 100
        self.attack_value = 10
        self.x = x * TILESIZE 
        self.y = y * TILESIZE 
        self.shouldiwalk = ""
        self.width = TILESIZE 
        self.height = TILESIZE 
        self.rect = self.image.get_rect() # able to get x and y coordinates
        self.rect.x = self.x
        self.rect.y = self.y
        self.x_change = 0
        self.y_change = 0


        self.animations_up = [  [
                            self.game.slime_spritesheet.get_image(0,0,self.width,self.height),
                            ],
                           [ ## beginning of walk animation
                           self.game.slime_spritesheet.get_image(0,0,self.width,self.height),
                           self.game.slime_spritesheet.get_image(0,50,self.width,self.height)
                            ]
                           ]
        
        self.animations_down = [  [
                            self.game.slime_spritesheet.get_image(0,0,self.width,self.height),
                            ],
                           [ ## beginning of walk animation
                           self.game.slime_spritesheet.get_image(0,0,self.width,self.height),
                           self.game.slime_spritesheet.get_image(0,50,self.width,self.height)
                            ]
                           ]
        
        self.animations_left = [  [
                            self.game.slime_spritesheet.get_image(0,0,self.width,self.height),
                            ],
                           [ ## beginning of walk animation
                           self.game.slime_spritesheet.get_image(0,0,self.width,self.height),
                           self.game.slime_spritesheet.get_image(0,100,self.width,self.height)
                            ]
                           ]
        
        self.animations_right = [  [
                            self.game.slime_spritesheet.get_image(0,0,self.width,self.height),
                            ],
                           [ ## beginning of walk animation
                           self.game.slime_spritesheet.get_image(0,0,self.width,self.height),
                           self.game.slime_spritesheet.get_image(0,150,self.width,self.height)
                            ]
                           ]
        self.animationlist = [self.animations_up,
                              self.animations_down,
                              self.animations_left,
                              self.animations_right
                              ]
    def start_walk_cycle(self):
        """ 
        if self.walkcycle == -1:
            self.walkcycle = 0
        """
        if self.walkcycle == -1:
            self.walkcycle = 0
            
    def walk(self):
        self.shouldiwalk = random.choice([True,False,False,False])
        if self.shouldiwalk:
            self.direction = random.choice([0,1,2,3])
            match self.direction:
                case 0:
                    if self.rect.y > 0:
                        self.y_change = -self.slimestep
                        self.start_walk_cycle()
                case 1:
                    if self.rect.y < MAPHEIGHT - TILESIZE:
                        self.y_change = self.slimestep
                        self.start_walk_cycle()
                case 2:
                    if self.rect.x > 0:
                        self.x_change = -self.slimestep
                        self.start_walk_cycle()
                case 3:
                    if self.rect.x < MAPWIDTH - TILESIZE:
                        self.x_change = self.slimestep
                        self.start_walk_cycle()

    def walkanimation(self):
        ### walkcycle is always set to a default value of -1 
        ### when not walking
        ### only runs if walk is not -1
        if self.walkcycle == -1:
            pass
        else:
            if not self.isattacking: # during attack animation, player will be still, so unable to check for is walking
                if self.x_change == 0 and self.y_change == 0:
                    self.image = self.animationlist[self.direction][0][0]
            if not self.isstrafe:
                if self.now - self.lastwalkanimation >= self.walkdelay + self.animationdelay + self.debuffdelay:
                    self.lastwalkanimation = self.now
                    self.rect.x += self.x_change
                    self.rect.y += self.y_change
                    if self.x_change != 0 or self.y_change != 0:
                        match self.direction:    
                            case 0 :  
                                self.match_walk_ani(self.animations_up[1])
                            case 1 :  
                                self.match_walk_ani(self.animations_down[1])                                    
                            case 2 :  
                                self.match_walk_ani(self.animations_left[1])                
                            case 3 :  
                                self.match_walk_ani(self.animations_right[1])
                                                        
    def update(self):
        self.now = pygame.time.get_ticks()
        self.walk()
        self.walkanimation()
        self.block_collision()
        self.x_change = 0
        self.y_change = 0
        self.action_reset()

                    
    def action_reset(self):
        if self.attackcycle >= 0:
            pass
        else:
            self.isattacking = False
            self.attackcycle = -1
        if self.walkcycle >= 0:
            pass
        else:
            self.x_change = 0
            self.y_change = 0
            self.walkcycle = -1
        
    def block_collision(self):
        collide = pygame.sprite.spritecollide(self,self.game.blocks, False) ## last argument is for block to disappear.
        if collide:
            if self.direction == 0:
                self.rect.y += TILESIZE/2
            if self.direction == 1:
                self.rect.y -= TILESIZE/2
            if self.direction == 2:
                self.rect.x += TILESIZE/2
            if self.direction == 3:
                self.rect.x -= TILESIZE/2