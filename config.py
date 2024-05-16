# -*- coding: utf-8 -*-
"""
Created on Sun May 12 16:45:18 2024

@author: zacwo
"""
import pygame

MAPWIDTH = 800
MAPHEIGHT = 600

TILESIZE = 50

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0,0,0)

FPS = 120
ABOVE_PLAYER = 4
PLAYER_LAYER = 3
BLOCKS_LAYER = 2
GROUND_LAYER = 1

tilemap = [
    '.............123',
    '.............456',
    '.............789',
    '.S..............',
    '.........P......',
    '................',
    '..........S.....',
    '................',
    '.123............',
    '.456............',
    '.789.........S..',
    '................'
    ]
