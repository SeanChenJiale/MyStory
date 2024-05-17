# -*- coding: utf-8 -*-
"""
Created on Sun May 12 12:39:57 2024

@author: Sean
"""
from config import *


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
        self._layer = PLAYER_LAYER 
        self.groups = self.game.all_sprites, self.game.enemies
        
        self.maxhealth = 100
        self.currenthealth = 100
        self.healthbarborder = slime_health_border(game, x, y)
        self.remaininghealthbar = slime_remaining_health(game, x, y)
        self.maxhealthbar = slime_max_healthbar(game, x, y) 
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x * TILESIZE 
        self.y = y * TILESIZE 
        
        self.direction = random.choice([0,1,2,3])
        
        self.width = TILESIZE 
        self.height = TILESIZE 
        
        self.image = self.game.slime_spritesheet.get_image(0,0,self.width,self.height)
        self.rect = self.image.get_rect() # able to get x and y coordinates
        self.rect.x = self.x
        self.rect.y = self.y

        self.lastattackanimation = 0
        self.lastwalkanimation = 0
        self.lastchangestrafe = 0
        self.strafechangedelay = 400
        self.lastdamagetaken = 0
        self.invulnerableuntil = 0
        self.attackcooldown = 0
        self.animationdelay = 150 #default animation delay.
        self.walkdelay = 400 # default tick delay.
        self.debuffdelay = 0
        self.walkcycle = -1
        self.attackcycle = -1 # default values 
        self.now = 0 # self.now is a counter to get the current game tick in pygame
        
        self.isalive = True
        self.isstrafe = False
        self.isidle = True
        self.isattacking = False
        self.attack_value = 10
        self.shouldiwalk = ""
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
    def checkhp(self):
        if self.currenthealth <= 0:
            self.isalive = False 

            
    def update(self):
        if self.isalive:
            self.checkhp()
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
                

class slime_health_border(pygame.sprite.Sprite):
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
        
        self.widthpadding = (TILESIZE - self.width) / 2
        self.heightpadding = (10 - self.height) / 2
        self.rect = self.image.get_rect()
        self.rect.x = self.x + self.widthpadding
        self.rect.y = self.y + TILESIZE + self.heightpadding
        
    def move(self):
        self.rect.x = self.game.slime.rect.x + self.widthpadding
        self.rect.y = self.game.slime.rect.y + TILESIZE + self.heightpadding
    
    def update(self):
        self.move()
        
class slime_max_healthbar(slime_health_border): ## child class from
## parent class slime_health_border
    def __init__ (self, game, x, y):
        super().__init__(game,x,y)
        
        self.width = 44
        self.height = 2
        self.padding = (TILESIZE - self.width) / 2
        self.heightpadding = (10 - self.height) / 2
        
        self.image = pygame.Surface([self.width,self.height])
        self.image.fill(red)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x + self.widthpadding
        self.rect.y = self.y + TILESIZE + self.heightpadding

        
class slime_remaining_health(slime_max_healthbar):
    ## child class from
    ## parent class slime_max_healthbar
    def __init__ (self, game, x, y):
        super().__init__(game,x,y)
        self._layer = REMAINING_HEALTH_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.image.fill(green)
    
    def widthchange(self):
        self.width = max (44 * (self.game.slime.currenthealth/self.game.slime.maxhealth), 1 )
        self.image = pygame.Surface([self.width,self.height])
        self.image.fill(green)
    def update(self):
        self.widthchange()
        self.move()
        