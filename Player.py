# -*- coding: utf-8 -*-
"""
Created on Sun May 12 12:37:28 2024

@author: zacwo
"""
import pygame
from config import *

class player(pygame.sprite.Sprite):
    def __init__ (self, game, x, y):
        self.lastattackanimation = 0
        self.lastwalkanimation = 0
        self.lastchangestrafe = 0
        self.strafechangedelay = 400
        self.attackcooldown = 0
        self.animationdelay = 150
        self.walkdelay = 100
        self.walkcycle = -1
        self.attackcycle = -1
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
        
    def match_walk_ani(self,walkanimationlist):
        match self.walkcycle:
            case 0:
                self.image = walkanimationlist[self.walkcycle]
                self.walkcycle +=1

            case 1:
                self.image = walkanimationlist[self.walkcycle]
                self.walkcycle = -1

                
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
                
    def update(self):
        self.now = pygame.time.get_ticks()
        self.strafe()
        self.attack()   
        self.walk()
        self.walkanimation()
        self.x_change = 0
        self.y_change = 0
        self.attackanimation()

    def strafe(self):
        pressed = pygame.key.get_pressed()
        if self.now - self.lastchangestrafe >= self.strafechangedelay:
            if pressed[pygame.K_s]:
                self.lastchangestrafe = self.now
                if self.isstrafe:
                    self.isstrafe = False
                else:
                    self.isstrafe = True
                    
    def walk(self):
        pressed = pygame.key.get_pressed()
        if not self.isattacking: 
            ### prevent movement when attacking                
            if self.isstrafe: 
                self.laststrafed = self.now
                if pressed[pygame.K_UP] and self.rect.y > 0:
                    self.y_change -= TILESIZE/2
                elif pressed[pygame.K_DOWN] and self.rect.y < MAPHEIGHT - TILESIZE:
                    self.y_change += TILESIZE/2   
                elif pressed[pygame.K_LEFT] and self.rect.x > 0:
                    self.x_change -= TILESIZE/2
                elif pressed[pygame.K_RIGHT] and self.rect.x < MAPWIDTH - TILESIZE:
                    self.x_change += TILESIZE/2  
            else:
                self.lastwalked = self.now
                if pressed[pygame.K_UP] and self.rect.y > 0:
                    self.y_change -= TILESIZE/2
                    self.direction = 0               
                elif pressed[pygame.K_DOWN] and self.rect.y < MAPHEIGHT - TILESIZE:
                    self.y_change += TILESIZE/2   
                    self.direction = 1                   
                elif pressed[pygame.K_LEFT] and self.rect.x > 0:
                    self.x_change -= TILESIZE/2
                    self.direction = 2                  
                elif pressed[pygame.K_RIGHT] and self.rect.x < MAPWIDTH - TILESIZE:
                    self.x_change += TILESIZE/2
                    self.direction = 3
    def walkanimation(self):
        ### walkcycle is always set to a default value of -1 
        ### when not walking
        ### only runs if walk is not -1
        if not self.isattacking:
            if self.x_change == 0 or self.y_change == 0:
                self.image = self.animationlist[self.direction][0][0]
        if not self.isstrafe:
            if self.now - self.lastwalkanimation >= self.walkdelay:
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
        elif self.isstrafe:
            if self.now - self.lastwalkanimation >= self.walkdelay + 50:
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
                                                
    def attackanimation(self):
        ### attackcycle is always set to a default value of -1 
        ### when not attacking
        ### only runs if attackcycle is not -1
        if self.attackcycle == -1:
            pass
            
        else: 
            if self.now - self.lastattackanimation >= self.animationdelay:
                self.lastattackanimation = self.now
                match self.direction:
                    case 0 :
                        attackanimationlist = self.animationlist[0][2]
                        self.match_attack_ani(attackanimationlist) 
             
                    case 1:
                        attackanimationlist = self.animationlist[1][2]
                        self.match_attack_ani(attackanimationlist)
                     
                    case 2:
                        attackanimationlist = self.animationlist[2][2]
                        self.match_attack_ani(attackanimationlist) 
            
                    case 3:
                        attackanimationlist = self.animationlist[3][2]
                        self.match_attack_ani(attackanimationlist)             
        

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
        if self.walkcycle >= 0:
            pass
        else:
            self.x_change = 0
            self.y_change = 0
            self.walkcycle = -1

        
                
                
            
