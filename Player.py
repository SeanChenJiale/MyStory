# -*- coding: utf-8 -*-
"""
Created on Sun May 12 12:37:28 2024

@author: Sean
"""
from config import *
from Weapon import *
class player(pygame.sprite.Sprite):
    def __init__ (self, game, x, y):
        self.movestep = TILESIZE 
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites , self.game.usergroup
        
        self.maxhealth = 100 ## note to put this before the healthbars
        self.currenthealth = 100 ## note to put this before the healthbars
        self.lastdamagetaken = 0
        self.invulnerableuntil = 0
    
        self.curreqweapon = weapon(game,x,y)
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.healthbarborder = player_health_border(game, x, y)
        self.maxhealthbar = player_max_healthbar(game, x, y) 
        self.remaininghealthbar = player_remaining_health(game, x, y)
        
        
        self.lastattackanimation = 0
        self.lastwalkanimation = 0
        self.lastchangestrafe = 0
        self.strafechangedelay = 400
        self.attackcooldown = 0
        self.animationdelay = 150 #default animation delay.
        self.walkdelay = 175 # default tick delay.
        self.debuffdelay = 0
        self.walkcycle = -1
        self.attackcycle = -1 # default values 
        self.direction = 1 # corresponds to list [u,d,l,r]
        self.now = 0 # self.now is a counter to get the current game tick in pygame
        
        self.isalive = True
        self.isstrafe = False
        self.isattacking = False
        self.iswalking = True
        self.iscollided = False

        self.attack_value = 10
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = 50 
        self.height = 50 
        
        self.image = self.game.player_spritesheet.get_image(50,0,self.width,self.height)
        self.rect = self.image.get_rect() # able to get x and y coordinates.
        self.rect.x = self.x
        self.rect.y = self.y
        
        self.tookdamage = False
        self.attackinstance = False
        self.attackingrect_x = self.x
        self.attackingrect_y = self.y
        
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
    def start_walk_cycle(self):
        """ 
        if self.walkcycle == -1:
            self.walkcycle = 0
        """
        if self.walkcycle == -1:
            self.walkcycle = 0
            
    def match_walk_ani(self,walkanimationlist):
        match self.walkcycle:
            case 0:
                self.image = walkanimationlist[self.walkcycle]
                self.walkcycle += 1

            case 1:
                self.image = walkanimationlist[self.walkcycle]
                self.walkcycle = -1

                
    def match_attack_ani(self,attackanimationlist):
        match self.attackcycle:
            case 0:
                self.image = attackanimationlist[self.attackcycle]
                self.attackcycle += 1
            case 1:
                self.image = attackanimationlist[self.attackcycle]
                self.attackcycle += 1
            case 2:
                self.image = attackanimationlist[self.attackcycle]
                self.attackcycle += 1
                self.attackinstance = True
            case 3:
                self.image = attackanimationlist[self.attackcycle - 1] ## delayer
                self.attackcycle = -1    
    def checkhp(self):
        if self.currenthealth <= 0:
            self.isalive = False 
            self.rect.x = -1000
            self.rect.y = -1000
            
    def update(self):
        if self.isalive:
            self.checkhp()
            self.now = pygame.time.get_ticks()
            self.strafe()
            self.attack()   
            self.walk()
            self.walkanimation()
            self.collide_block()
            self.collide_enemy()
            self.x_change = 0
            self.y_change = 0
            self.attackanimation()
            self.action_reset()
            
            

    
    def strafe(self):
        pressed = pygame.key.get_pressed()
        if self.now - self.lastchangestrafe >= self.strafechangedelay + self.debuffdelay:
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
                    self.y_change -= self.movestep
                    self.start_walk_cycle()
                elif pressed[pygame.K_DOWN] and self.rect.y < MAPHEIGHT - self.height:
                    self.y_change += self.movestep
                    self.start_walk_cycle()
                elif pressed[pygame.K_LEFT] and self.rect.x > 0:
                    self.x_change -= self.movestep
                    self.start_walk_cycle()
                elif pressed[pygame.K_RIGHT] and self.rect.x < MAPWIDTH - self.width:
                    self.x_change += self.movestep 
                    self.start_walk_cycle()
            else:
                self.lastwalked = self.now
                if pressed[pygame.K_UP]:
                    self.direction = 0   
                    if self.rect.y > 0:
                        self.y_change -= self.movestep
                        self.start_walk_cycle()
                elif pressed[pygame.K_DOWN]:
                    self.direction = 1   
                    if self.rect.y < MAPHEIGHT - self.height:
                        self.y_change += self.movestep   
                        self.start_walk_cycle()
                elif pressed[pygame.K_LEFT]:
                    self.direction = 2  
                    if self.rect.x > 0:
                        self.x_change -= self.movestep
                        self.start_walk_cycle()
                elif pressed[pygame.K_RIGHT]:
                    self.direction = 3
                    if self.rect.x < MAPWIDTH - self.width:
                        self.x_change += self.movestep
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
                if self.now - self.lastwalkanimation >= self.walkdelay + self.debuffdelay:
                    self.lastwalkanimation = self.now
                    self.rect.x += self.x_change
                    self.rect.y += self.y_change
                    if self.x_change != 0 or self.y_change != 0:
                        match self.direction:    
                            case 0 :  
                                self.match_walk_ani(self.animations_up[1])
                                self.iswalking = True
                            case 1 :  
                                self.match_walk_ani(self.animations_down[1])      
                                self.iswalking = True
                            case 2 :  
                                self.match_walk_ani(self.animations_left[1])
                                self.iswalking = True
                            case 3 :  
                                self.match_walk_ani(self.animations_right[1])
                                self.iswalking = True
            elif self.isstrafe:
                if self.now - self.lastwalkanimation >= self.walkdelay + 50 + self.debuffdelay:
                    self.lastwalkanimation = self.now
                    self.rect.x += self.x_change
                    self.rect.y += self.y_change
                    if self.x_change != 0 or self.y_change != 0:
                        match self.direction:    
                            case 0 :  
                                self.match_walk_ani(self.animations_up[1])
                                self.iswalking = True
                            case 1 :
                                self.match_walk_ani(self.animations_down[1])
                                self.iswalking = True                                    
                            case 2 :  
                                self.match_walk_ani(self.animations_left[1])
                                self.iswalking = True
                            case 3 :  
                                self.match_walk_ani(self.animations_right[1])
                                self.iswalking = True
                                                    
    def attackanimation(self):
        ### attackcycle is always set to a default value of -1 
        ### when not attacking
        ### only runs if attackcycle is not -1
        if self.attackcycle == -1:
            pass
            
        else: 
            if self.now - self.lastattackanimation >= self.animationdelay + self.debuffdelay:
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

    def collide_block(self):
        pressed = pygame.key.get_pressed()
        collide = pygame.sprite.spritecollide(self,self.game.blocks, False) ## last argument is for block to disappear.
        if collide:
            self.iscollided = True
            #### changing elifs to ifs give an amazing interaction when approacting from the left and right of things.
            if pressed[pygame.K_UP]:
                self.rect.y += self.movestep
            elif pressed[pygame.K_DOWN]:
                self.rect.y -= self.movestep
            elif pressed[pygame.K_LEFT]:
                self.rect.x += self.movestep
            elif pressed[pygame.K_RIGHT]:
                self.rect.x -= self.movestep
        else:
            self.iscollided = False
    def collide_enemy(self):
        pressed = pygame.key.get_pressed()
        collide = pygame.sprite.spritecollide(self,self.game.enemies, False) ## last argument is for block to disappear.
        for enemy in collide:
            
            if self.now > self.invulnerableuntil:
                self.currenthealth -= enemy.attack_value
                self.lastdamagetaken = self.now
                self.invulnerableuntil = self.lastdamagetaken + 1000
        if collide:
            #### changing elifs to ifs give an amazing interaction when approacting from the left and right of things.
            self.iscollided = True
            if pressed[pygame.K_UP]:
                self.rect.y += self.movestep
            elif pressed[pygame.K_DOWN]:
                self.rect.y -= self.movestep
            elif pressed[pygame.K_LEFT]:
                self.rect.x += self.movestep
            elif pressed[pygame.K_RIGHT]:
                self.rect.x -= self.movestep
        else:
            self.iscollided = False
class player_health_border(pygame.sprite.Sprite):
    def __init__ (self, game, x, y):
        self.game = game
        self._layer = HEALTH_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x * TILESIZE 
        self.y = y * TILESIZE
        
        self.width = 48
        self.height = 4
        
        self.image = pygame.Surface([self.width,self.height])
        self.image.fill(darkgrey)
        
        self.widthpadding = (50 - self.width) / 2
        self.heightpadding = (10 - self.height) / 2
        self.rect = self.image.get_rect()
        self.rect.x = self.x + self.widthpadding
        self.rect.y = self.y + 50 + self.heightpadding
        
    def move(self):
        self.rect.x = self.game.player.rect.x + self.widthpadding
        self.rect.y = self.game.player.rect.y + 50 + self.heightpadding
    
    def update(self):
        self.move()
        
class player_max_healthbar(player_health_border): ## child class from
## parent class player_health_border
    def __init__ (self, game, x, y):
        super().__init__(game,x,y)
        
        self.width = 44
        self.height = 2
        self.padding = (50 - self.width) / 2
        self.heightpadding = (10 - self.height) / 2
        
        self.image = pygame.Surface([self.width,self.height])
        self.image.fill(red)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x + self.widthpadding
        self.rect.y = self.y + 50 + self.heightpadding

        
class player_remaining_health(player_max_healthbar):
    ## child class from
    ## parent class player_max_healthbar
    def __init__ (self, game, x, y):
        super().__init__(game, x, y)
        self._layer = REMAINING_HEALTH_LAYER
        
        self.image = pygame.Surface([self.width,self.height])
        self.image.fill(green)
        self.rect = self.image.get_rect()
        self.rect.x = self.x + self.widthpadding
        self.rect.y = self.y + 50 + self.heightpadding
    def widthchange(self):
        self.width = max (44 * (self.game.player.currenthealth/self.game.player.maxhealth), 1 )
        self.image = pygame.Surface([self.width,self.height])
        self.image.fill(green)
    def update(self):
        self.widthchange()
        self.move()
        

