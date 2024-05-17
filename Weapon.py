# -*- coding: utf-8 -*-
"""
Created on Fri May 17 09:20:05 2024

@author: ChenS11
"""
from config import *
class weapon (pygame.sprite.Sprite):
    def __init__ (self,game,x,y):
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.attack_value = 15
        self.width = TILESIZE
        self.height = TILESIZE
        
        self.x = x * TILESIZE 
        self.y = y * TILESIZE 
        
        self.weaponrange = TILESIZE/2
        self.image = pygame.Surface([self.width,self.height])
        self.rect = self.image.get_rect()
        self.rect.x = self.x 
        self.rect.y = self.y 
        
        self.x_change = 0
        self.y_change = 0
        
        self.image.fill((0,0,1))
        self.image.set_colorkey((0,0,1))
        
    def move(self):
        self.rect.x = self.game.player.rect.x 
        self.rect.y = self.game.player.rect.y
    
    def attack(self):
        count = 0
        if self.game.player.attackinstance: # basically player has a damageinstance init
        ## it changes on the 3rd frame of the attack.

            # print(f"{self.game.player.attackinstance}, {count} ,currentlyfacing {self.game.player.direction}")
            match self.game.player.direction:
                case 0:
                    self.y_change = -self.weaponrange
                case 1:
                    self.y_change = self.weaponrange
                case 2:
                    self.x_change = -self.weaponrange
                case 3:
                    self.x_change = self.weaponrange
                    
    def action_reset(self):
        self.y_change = 0
        self.x_change = 0
        self.game.player.attackinstance = False
        
    def attack_shift(self):
        if self.x_change != 0:
            self.rect.x += self.x_change
        if self.y_change != 0:
            self.rect.y += self.y_change
            
    def undo_attack_shift(self):
        if self.x_change != 0:
            self.rect.x -= self.x_change
        if self.y_change != 0:
            self.rect.y -= self.y_change         

    def collision_check(self):
        collide = pygame.sprite.spritecollide(self,self.game.enemies, False) ## last argument is for block to disappear.
        for enemy in collide:
            if self.game.player.now > enemy.invulnerableuntil:
                enemy.currenthealth -= self.attack_value
                enemy.lastdamagetaken = self.game.player.now
                enemy.invulnerableuntil = enemy.lastdamagetaken + 1000
                if enemy.currenthealth <= 0:
                    enemy.isalive = False
                    enemy.rect.x = -1000
                    enemy.rect.y = -1000
    def update(self):        
        self.move()
        self.attack()
        self.attack_shift()
        self.collision_check()
        self.undo_attack_shift()
        self.action_reset()
        