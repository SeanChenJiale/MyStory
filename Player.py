# -*- coding: utf-8 -*-
"""
Created on Sun May 12 12:37:28 2024

@author: zacwo
"""
import pygame
from config import *

class player(pygame.sprite.Sprite):
    def match_attack_ani(self,attackanimationlist):
        match self.attackcycle:
            case 0:
                self.image = attackanimationlist[self.attackcycle]
                self.attackcycle +=1
            case 1:
                self.image = attackanimationlist[self.attackcycle]
                self.attackcycle +=1
            case 2:
                self.image = attackanimationlist[self.attackcycle]
                self.attackcycle += 1
            case 3:
                self.image = attackanimationlist[self.attackcycle - 1] ## delayer
                self.attackcycle = -1    
                
    def __init__ (self, game, x, y):
        self.lastattackanimation = 0
        self.lastwalked = 0
        self.laststrafed = 0
        self.lastchangestrafe = 0
        self.walkcooldown = 100
        self.strafecooldown = 200
        self.strafechangedelay = 400
        self.attackcooldown = 0
        self.animationdelay = 150
        self.walkcycle = 0
        self.attackcycle = -1
        self.iswalking = False
        self.isstrafe = False
        self.isidle = True
        self.isattacking = False
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x * TILESIZE 
        self.y = y * TILESIZE 
        self.now = 0
        self.direction = 1

        self.width = TILESIZE 
        self.height = TILESIZE 
        
        self.image = self.game.player_spritesheet.get_image(50,0,self.width,self.height)
        self.rect = self.image.get_rect() # able to get x and y coordinates.
        self.rect.x = self.x
        self.rect.y = self.y
        
        self.x_change = 0
        self.y_change = 0
        self.animations_up = [  [
                            self.game.player_spritesheet.get_image(0,0,self.width,self.height),
                            ],
                           [ ## beginning of walk animation
                           self.game.player_spritesheet.get_image(0,50,self.width,self.height),
                           self.game.player_spritesheet.get_image(0,100,self.width,self.height)
                            ],
                           [ ## beginning of attack animation
                           self.game.player_spritesheet.get_image(0,150,self.width,self.height),
                           self.game.player_spritesheet.get_image(0,200,self.width,self.height),
                           self.game.player_spritesheet.get_image(0,250,self.width,self.height)
                            ]
                           ]
        
        self.animations_down = [  [
                            self.game.player_spritesheet.get_image(50,0,self.width,self.height),
                            ],
                           [ ## beginning of walk animation
                           self.game.player_spritesheet.get_image(50,50,self.width,self.height),
                           self.game.player_spritesheet.get_image(50,100,self.width,self.height)
                            ],
                           [ ## beginning of attack animation
                           self.game.player_spritesheet.get_image(50,150,self.width,self.height),
                           self.game.player_spritesheet.get_image(50,200,self.width,self.height),
                           self.game.player_spritesheet.get_image(50,250,self.width,self.height)
                            ]
                           ]
        
        self.animations_left = [  [
                            self.game.player_spritesheet.get_image(100,0,self.width,self.height),
                            ],
                           [ ## beginning of walk animation
                           self.game.player_spritesheet.get_image(100,50,self.width,self.height),
                           self.game.player_spritesheet.get_image(100,100,self.width,self.height)
                            ],
                           [ ## beginning of attack animation
                           self.game.player_spritesheet.get_image(100,150,self.width,self.height),
                           self.game.player_spritesheet.get_image(100,200,self.width,self.height),
                           self.game.player_spritesheet.get_image(100,250,self.width,self.height)
                            ]
                           ]
        
        self.animations_right = [  [
                            self.game.player_spritesheet.get_image(150,0,self.width,self.height),
                            ],
                           [ ## beginning of walk animation
                           self.game.player_spritesheet.get_image(150,50,self.width,self.height),
                           self.game.player_spritesheet.get_image(150,100,self.width,self.height)
                            ],
                           [ ## beginning of attack animation
                           self.game.player_spritesheet.get_image(150,150,self.width,self.height),
                           self.game.player_spritesheet.get_image(150,200,self.width,self.height),
                           self.game.player_spritesheet.get_image(150,250,self.width,self.height)
                            ]
                           ]
        self.animationlist = [self.animations_up,
                              self.animations_down,
                              self.animations_left,
                              self.animations_right
                              ]
    def update(self):
        self.now = pygame.time.get_ticks()
        self.strafe()
        self.attack()   
        self.move()
        self.rect.x += self.x_change
        self.rect.y += self.y_change
        self.x_change = 0
        self.y_change = 0
        self.animation()

    def strafe(self):
        pressed = pygame.key.get_pressed()
        if self.now - self.lastchangestrafe >= self.strafechangedelay:
            if pressed[pygame.K_s]:
                self.lastchangestrafe = self.now
                if self.isstrafe:
                    self.isstrafe = False
                else:
                    self.isstrafe = True
    def move(self):
        pressed = pygame.key.get_pressed()
        if not self.isattacking: 
            ### prevent movement when attacking                
            if self.isstrafe: 
                if self.now - self.laststrafed >= self.strafecooldown:
                    self.laststrafed = self.now
                    if pressed[pygame.K_UP]:
                        self.iswalking = True
                        self.y_change -= TILESIZE/2
                        
                    elif pressed[pygame.K_DOWN]:
                        self.iswalking = True
                        self.y_change += TILESIZE/2   
        
                    elif pressed[pygame.K_LEFT]:
                        self.iswalking = True
                        self.x_change -= TILESIZE/2
        
                    elif pressed[pygame.K_RIGHT]:
                        self.iswalking = True
                        self.x_change += TILESIZE/2
    
            elif self.now - self.lastwalked >= self.walkcooldown:
                self.lastwalked = self.now
                if pressed[pygame.K_UP]:
                    self.iswalking = True
                    self.y_change -= TILESIZE/2
                    self.walkcycle += 1
                    self.direction = 0
                    
                elif pressed[pygame.K_DOWN]:
                    self.iswalking = True
                    self.y_change += TILESIZE/2   
                    self.walkcycle += 1
                    self.direction = 1
                    
                elif pressed[pygame.K_LEFT]:
                    self.iswalking = True
                    self.x_change -= TILESIZE/2
                    self.walkcycle += 1
                    self.direction = 2
                    
                elif pressed[pygame.K_RIGHT]:
                    self.iswalking = True
                    self.x_change += TILESIZE/2
                    self.walkcycle += 1
                    self.direction = 3

    def animation(self):
        match self.direction:
            case 0 :

                walkanimationlist = self.animationlist[0][1]
                attackanimationlist = self.animationlist[0][2]
                if self.iswalking:
                    match self.walkcycle:
                        case 0:
                            self.image = walkanimationlist[self.walkcycle]
                            self.walkcycle +=1
                        case 1:
                            self.image = walkanimationlist[self.walkcycle]
                            self.walkcycle = 0
                elif self.attackcycle >= 0:
                    if self.now - self.lastattackanimation >= self.animationdelay:
                        self.lastattackanimation = self.now
                        self.match_attack_ani(attackanimationlist) 
                else:
                    self.image = self.animationlist[0][0][0]

                   
                        
                    
                    
            case 1:
                walkanimationlist = self.animationlist[1][1]
                attackanimationlist = self.animationlist[1][2]

                if self.iswalking:
                    match self.walkcycle:
                        case 0:
                            self.image = walkanimationlist[self.walkcycle]
                            self.walkcycle +=1
                        case 1:
                            self.image = walkanimationlist[self.walkcycle]
                            self.walkcycle = 0
                elif self.attackcycle >= 0:
                    if self.now - self.lastattackanimation >= self.animationdelay:
                        self.lastattackanimation = self.now
                        self.match_attack_ani(attackanimationlist)
                else:
                    self.image = self.animationlist[1][0][0]
             
            case 2:
                walkanimationlist = self.animationlist[2][1]
                attackanimationlist = self.animationlist[2][2]
                if self.iswalking:

                    match self.walkcycle:
                        case 0:
                            self.image = walkanimationlist[self.walkcycle]
                            self.walkcycle +=1
                        case 1:
                            self.image = walkanimationlist[self.walkcycle]
                            self.walkcycle = 0
                elif self.attackcycle >= 0:
                    if self.now - self.lastattackanimation >= self.animationdelay:
                        self.lastattackanimation = self.now
                        self.match_attack_ani(attackanimationlist) 
                else:
                    self.image = self.animationlist[2][0][0]

                                
            case 3:
                walkanimationlist = self.animationlist[3][1]
                attackanimationlist = self.animationlist[3][2]
                if self.iswalking:

                    match self.walkcycle:
                        case 0:
                            self.image = walkanimationlist[self.walkcycle]
                            self.walkcycle +=1
                        case 1:
                            self.image = walkanimationlist[self.walkcycle]
                            self.walkcycle = 0
                elif self.attackcycle >= 0 :
                    
                    
                    if self.now - self.lastattackanimation >= self.animationdelay:
                        self.lastattackanimation = self.now
                        self.match_attack_ani(attackanimationlist) 
                else:
                    self.image = self.animationlist[3][0][0]

    def attack(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_c]:
            self.isattacking = True
            if self.attackcycle == -1:
                self.attackcycle = 0
                
    def reset(self):
        if self.attackcycle >= 0:
            pass
        else:
            self.isattacking = False
            self.attackcycle = -1
        self.iswalking = False
                
                
            
